"""Reading and writing JSON files."""

import json
import tempfile
import os


def write_json(path, data, pretty=True):
    """Write data to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2 if pretty else None)
    print(f"Wrote JSON to {path}")


def read_json(path):
    """Read and parse a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def json_roundtrip(data):
    """Serialize to string and back."""
    text = json.dumps(data, sort_keys=True)
    parsed = json.loads(text)
    print(f"Original:  {data}")
    print(f"JSON str:  {text}")
    print(f"Parsed:    {parsed}")
    return parsed


if __name__ == "__main__":
    filepath = os.path.join(tempfile.gettempdir(), "demo.json")
    config = {"name": "myapp", "version": 1, "features": ["auth", "api"]}
    write_json(filepath, config)
    loaded = read_json(filepath)
    print(f"Loaded: {loaded}")
    os.remove(filepath)
    print("-" * 40)
    json_roundtrip({"key": [1, 2, 3], "flag": True})
