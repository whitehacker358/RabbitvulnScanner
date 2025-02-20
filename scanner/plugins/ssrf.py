async def check_ssrf(session, url, logger, fetch):
    payload = "http://169.254.169.254/latest/meta-data/"
    response, status = await fetch(session, url, params={"url": payload})
    if response and ("iam" in response.lower() or "instance-id" in response.lower()):
        logger.info(f"SSRF detected at {url}")
        return {"type": "SSRF", "url": url, "poc": payload, "depth": "deep"}
    return None
