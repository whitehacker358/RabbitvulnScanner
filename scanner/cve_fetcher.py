import aiohttp

async def fetch_cve_data(session, logger):
    url = "https://cve.circl.lu/api/last"
    try:
        async with session.get(url) as response:
            data = await response.json()
            logger.debug(f"CVE API response: {data}")
            # Handle case where data might not be a list or keys differ
            if not isinstance(data, list):
                logger.error("CVE API returned unexpected format")
                return []
            return [{"id": cve.get("cve", "Unknown"), "description": cve.get("summary", "No summary")} for cve in data]
    except Exception as e:
        logger.error(f"Error fetching CVE data: {e}")
        return []
