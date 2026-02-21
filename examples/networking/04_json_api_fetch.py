"""Fetch and parse JSON from a URL (conceptual demo)."""

import json
from urllib.request import urlopen, Request
from urllib.error import URLError


def fetch_json(url, timeout=10):
    """Fetch JSON data from a URL and return as Python dict."""
    request = Request(url, headers={"Accept": "application/json"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except (URLError, json.JSONDecodeError) as e:
        return {"error": str(e)}


def pretty_print_json(data, indent=2):
    """Pretty print a JSON-serializable object."""
    return json.dumps(data, indent=indent, sort_keys=True)


def extract_fields(data, fields):
    """Extract specific fields from a JSON response dict."""
    return {f: data.get(f) for f in fields if f in data}


if __name__ == "__main__":
    sample = {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}
    print("Sample JSON response:")
    print(pretty_print_json(sample))
    print("\nExtracted fields:", extract_fields(sample, ["users", "missing"]))
    print("\nTo fetch real data: fetch_json('https://api.example.com/data')")
