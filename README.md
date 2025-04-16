
---

### `README.md`

```markdown
# CVE API using Flask

This is a simple Flask-based API that serves CVE data from a local `nvdcve-1.1-recent.json` file. Each endpoint gives you a specific view into the data such as CVE IDs, base scores, exploitability scores, impact scores, and attack vectors.

## Requirements

- Python 3.7+
- Flask

Install Flask using pip:

```bash
pip install flask
```

## Files

- `app.py`: Contains the Flask API.
- `nvdcve-1.1-recent.json`: The local CVE data file downloaded from the NVD.

## How to Run

Make sure both `app.py` and `nvdcve-1.1-recent.json` are in the same directory. Then run:

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`.

## Available API Endpoints

Each route returns JSON data.

### GET `/api/cves`

Returns a list of all CVE IDs.

### GET `/api/base-scores`

Returns a list of CVE IDs and their CVSS base scores.

### GET `/api/exploitability-scores`

Returns a list of CVE IDs and their exploitability scores.

### GET `/api/impact-scores`

Returns a list of CVE IDs and their impact scores.

### GET `/api/attack-vectors`

Returns a list of CVE IDs and their attack vectors.

## Notes

- Make sure the JSON file is up to date. You can get the latest from: https://nvd.nist.gov/vuln/data-feeds
- This is meant for local or dev use, but you can easily extend it with filters or deployment support if needed.
```

---

