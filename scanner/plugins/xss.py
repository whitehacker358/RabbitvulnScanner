async def check_xss(session, url, logger, fetch):
    payloads = [
        "<script>alert(\"RabbitXSS\")</script>",
        "\";alert(\"RabbitXSS\");//",
        "<img src=x onerror=alert(\"RabbitXSS\")>",
    ]
    for payload in payloads:
        response, status = await fetch(session, url, params={"q": payload})
        if response and payload in response:
            logger.info(f"XSS detected at {url}")
            return {"type": "XSS", "url": url, "poc": payload, "depth": "deep"}
    return None
