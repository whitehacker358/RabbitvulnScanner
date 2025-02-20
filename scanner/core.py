import asyncio
import aiohttp
from urllib.parse import urlparse
from .plugins.xss import check_xss
from .plugins.sqli import check_sqli
from .plugins.ssrf import check_ssrf
from .cve_fetcher import fetch_cve_data

class RabbitVulnScanner:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.results = []
        self.plugins = [check_xss, check_sqli, check_ssrf]
        self.semaphore = asyncio.Semaphore(config["threads"])

    async def fetch(self, session, url, method="GET", params=None):
        async with self.semaphore:
            try:
                if method == "GET":
                    async with session.get(url, params=params, timeout=self.config["timeout"]) as resp:
                        return await resp.text(), resp.status
            except Exception as e:
                self.logger.error(f"Fetch error at {url}: {str(e)}")
                return None, None

    async def crawl(self, session, url, depth):
        if depth <= 0:
            return set()
        urls = set([url])
        async with session.get(url) as resp:
            if resp.status == 200:
                text = await resp.text()
                for link in self.extract_links(text, url):
                    urls.add(link)
                    if len(urls) < 50:
                        urls.update(await self.crawl(session, link, depth - 1))
        return urls

    def extract_links(self, html, base_url):
        from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
        import warnings
        warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
        soup = BeautifulSoup(html, "html.parser")
        base = urlparse(base_url)
        links = set()
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("/"):
                href = f"{base.scheme}://{base.netloc}{href}"
            if base.netloc in href:
                links.add(href)
        return links

    async def run(self):
        url = self.config["target"]
        proxy = self.config.get("proxy")
        async with aiohttp.ClientSession(proxy=proxy) as session:
            urls = await self.crawl(session, url, self.config["depth"])
            self.logger.info(f"Crawled {len(urls)} URLs")
            cve_data = await fetch_cve_data(session, self.logger)
            tasks = [self.run_plugin(session, plugin, u) for u in urls for plugin in self.plugins]
            await asyncio.gather(*tasks)
            for cve in cve_data[:10]:
                self.results.append({"cve": cve["id"], "desc": cve["description"]})
        return self.results

    async def run_plugin(self, session, plugin, url):
        result = await plugin(session, url, self.logger, self.fetch)
        if result:
            self.results.append(result)
