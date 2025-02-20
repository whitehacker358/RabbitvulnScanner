def generate_poc(vuln_type, url, payload):
    if vuln_type == "XSS":
        return f"Inject `{payload}` at {url} to trigger XSS"
    elif vuln_type == "SQLi":
        return f"Use `{payload}` at {url} to exploit SQLi (test with DB tools)"
    elif vuln_type == "SSRF":
        return f"Send `{payload}` to {url} to access internal services"
    return "No PoC available"
