import aiohttp

async def fetch_cve_data(session, logger):
    url = "https://cve.circl.lu/api/last"
    try:
        async with session.get(url) as response:
            data = await response.json()
            return [{"id": cve["id"], "description": cve["summary"]} for cve in data]
    except Exception as e:
        logger.error(f"Error fetching CVE data: {e}")
        return []
