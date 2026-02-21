"""Read and parse JSON from files and strings."""

import json


def parse_json_string(json_str):
    """Parse a JSON string into a Python object."""
    return json.loads(json_str)


def read_json_file(filepath):
    """Read and parse a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)


def safe_parse(json_str, default=None):
    """Safely parse JSON, returning default on failure."""
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return default


def extract_nested(data, path, default=None):
    """Extract a value from nested JSON using dot-separated path."""
    keys = path.split(".")
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data


if __name__ == "__main__":
    json_str = '{"name": "Alice", "age": 30, "address": {"city": "NYC"}}'
    data = parse_json_string(json_str)
    print(f"Parsed: {data}")
    print(f"Name: {data['name']}")
    print(f"City: {extract_nested(data, 'address.city')}")
    print(f"Safe parse invalid: {safe_parse('not json', {})}")
    print(f"Safe parse valid: {safe_parse('[1,2,3]')}")
