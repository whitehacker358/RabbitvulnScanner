# RabbitvulnScanner
A deep, fast vulnerability scanner surpassing Nuclei in speed and effectiveness.

## Features
- **Deep Scanning**: Crawls and checks for complex vulns (e.g., blind SQLi, SSRF).
- **Faster than Nuclei**: Optimized async engine with dynamic concurrency.
- **Effective**: Broad coverage with PoCs and CVE integration (up to Feb 2025).
- **Inspired by**: xRay’s speed ([xRay_Scanner_Cracked_1.9.3](https://github.com/TcherB31/xRay_Scanner_Cracked_1.9.3)).

## Installation
1. Clone: `git clone https://github.com/yourusername/RabbitvulnScanner.git`
2. Install: `pip install -r requirements.txt`
3. Run: `python main.py`

## Usage
Enter a target URL (e.g., `http://example.com`). Results in `rabbit_report.html`.

## Why Better Than Nuclei?
- Deeper analysis with dynamic payloads vs. static templates.
- Faster execution with adaptive crawling and concurrency.

## License
MIT
