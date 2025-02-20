#!/usr/bin/env python3
import asyncio
import argparse
from scanner.core import RabbitVulnScanner
from utils.logger import setup_logger
from utils.report import generate_report

def main():
    parser = argparse.ArgumentParser(description="RabbitvulnScanner: A deep, fast vulnerability scanner")
    parser.add_argument("target", help="Target URL (e.g., http://example.com)")
    parser.add_argument("--proxy", help="Proxy URL (e.g., http://proxy:8080)")
    parser.add_argument("--deep", type=int, default=3, help="Crawl depth (default: 3)")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    args = parser.parse_args()

    logger = setup_logger(verbose=args.verbose)
    config = {
        "target": args.target,
        "threads": 20,
        "timeout": 2,
        "depth": args.deep,
        "proxy": args.proxy
    }
    scanner = RabbitVulnScanner(config, logger)
    logger.info(f"Starting RabbitvulnScanner on {args.target}")
    results = asyncio.run(scanner.run())
    generate_report(results, "rabbit_report.html")
    logger.info("Scan completed. Report saved as rabbit_report.html")

if __name__ == "__main__":
    main()
