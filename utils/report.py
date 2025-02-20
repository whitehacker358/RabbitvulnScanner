from poc.poc_generator import generate_poc

def generate_report(results, output_file):
    html = "<html><body><h1>RabbitvulnScanner Report</h1><table border=\"1\">"
    html += "<tr><th>Type</th><th>URL</th><th>PoC</th><th>Description</th></tr>"
    for result in results:
        poc = generate_poc(result.get("type", "CVE"), result.get("url", ""), result.get("poc", ""))
        desc = result.get("desc", "Deep vulnerability check")
        html += f"<tr><td>{result.get(type, CVE)}</td><td>{result.get(url, result.get(cve, ))}</td><td>{poc}</td><td>{desc}</td></tr>"
    html += "</table></body></html>"
    with open(output_file, "w") as f:
        f.write(html)
