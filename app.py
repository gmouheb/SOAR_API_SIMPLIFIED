from flask import Flask, jsonify
from data_loader import load_cve_data

app = Flask(__name__)
cve_items = load_cve_data()

@app.route('/api/cves', methods=['GET'])
def get_all_cves():
    cves = [
        {
            'id': item['cve']['CVE_data_meta']['ID'],
            'baseScore': item.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('baseScore'),
            'exploitabilityScore': item.get('impact', {}).get('baseMetricV3', {}).get('exploitabilityScore'),
            'impactScore': item.get('impact', {}).get('baseMetricV3', {}).get('impactScore'),
            'attackVector': item.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('attackVector')
        }
        for item in cve_items
        if item.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('baseScore') is not None
        and item.get('impact', {}).get('baseMetricV3', {}).get('exploitabilityScore') is not None
        and item.get('impact', {}).get('baseMetricV3', {}).get('impactScore') is not None
        and item.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('attackVector') is not None
    ]
    return jsonify(cves)

@app.route('/api/base-scores', methods=['GET'])
def get_base_scores():
    base_scores = [
        {
            'id': item['cve']['CVE_data_meta']['ID'],
        }
        for item in cve_items
        if item.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('baseScore') is not None
    ]
    return jsonify(base_scores)

@app.route('/api/exploitability-scores', methods=['GET'])
def get_exploitability_scores():
    exploit_scores = [
        {
            'id': item['cve']['CVE_data_meta']['ID'],
            'exploitabilityScore': item.get('impact', {}).get('baseMetricV3', {}).get('exploitabilityScore')
        }
        for item in cve_items
        if item.get('impact', {}).get('baseMetricV3', {}).get('exploitabilityScore') is not None
    ]
    return jsonify(exploit_scores)

@app.route('/api/impact-scores', methods=['GET'])
def get_impact_scores():
    impact_scores = [
        {
            'id': item['cve']['CVE_data_meta']['ID'],
            'impactScore': item.get('impact', {}).get('baseMetricV3', {}).get('impactScore')
        }
        for item in cve_items
        if item.get('impact', {}).get('baseMetricV3', {}).get('impactScore') is not None
    ]
    return jsonify(impact_scores)

@app.route('/api/attack-vectors', methods=['GET'])
def get_attack_vectors():
    vectors = [
        {
            'id': item['cve']['CVE_data_meta']['ID'],
            'attackVector': item.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('attackVector')
        }
        for item in cve_items
        if item.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('attackVector') is not None
    ]
    return jsonify(vectors)

if __name__ == '__main__':
    app.run(debug=True)
