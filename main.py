#!/usr/bin/env python3
import asyncio
from scanner.core import RabbitVulnScanner
from utils.logger import setup_logger
from utils.report import generate_report

def main():
    logger = setup_logger()
    target = input("Enter target URL (e.g., http://example.com): ")
    config = {"target": target, "threads": 20, "timeout": 2, "depth": 3}
    scanner = RabbitVulnScanner(config, logger)
    logger.info(f"Starting RabbitvulnScanner on {target}")
    results = asyncio.run(scanner.run())
    generate_report(results, "rabbit_report.html")
    logger.info("Scan completed. Report saved as rabbit_report.html")

if __name__ == "__main__":
    main()
