# RabbitvulnScanner
A deep, fast vulnerability scanner surpassing Nuclei in speed and effectiveness.

## Features
- **Deep Scanning**: Crawls and checks for complex vulns (e.g., blind SQLi, SSRF).
- **Faster than Nuclei**: Optimized async engine with dynamic concurrency.
- **Effective**: Broad coverage with PoCs and CVE integration (up to Feb 2025).
- **Verbose Output**: Vulnerabilities in red (inspired by xRay).

## Installation
1. Clone: `git clone https://github.com/whitehacker358/RabbitvulnScanner.git`
2. Install: `pip install -r requirements.txt`
3. Run: `python main.py <target> [options]`

## Usage
Run with a target URL and optional flags:
- `--proxy <url>`: Use a proxy (e.g., `http://proxy:8080`).
- `--deep <int>`: Set crawl depth (default: 3).
- `--verbose`: Show detailed output.

### Examples
- Basic scan: `python main.py https://sattamatkachart.in`
- With proxy: `python main.py https://sattamatkachart.in --proxy http://localhost:8080`
- Deep scan: `python main.py https://sattamatkachart.in --deep 5 --verbose`

### Output
- Terminal logs show progress (vulnerabilities in red).
- Results saved in `rabbit_report.html`.

## Why Better Than Nuclei?
- Deeper analysis with dynamic payloads vs. static templates.
- Faster execution with adaptive crawling and concurrency.

## License
MIT
