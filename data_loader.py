import json

def load_cve_data(path='nvdcve-1.1-recent.json'):
    with open(path, 'r') as f:
        data = json.load(f)
    return data.get("CVE_Items", [])
