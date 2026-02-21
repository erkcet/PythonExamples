"""Write Python objects to JSON files and strings."""

import json
import os


def to_json_string(data, pretty=False):
    """Convert Python object to JSON string."""
    kwargs = {"indent": 2, "sort_keys": True} if pretty else {}
    return json.dumps(data, **kwargs)


def write_json_file(filepath, data, pretty=True):
    """Write data to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2 if pretty else None, sort_keys=True)


def append_to_json_list(filepath, item):
    """Append an item to a JSON array file."""
    data = []
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            data = json.load(f)
    data.append(item)
    write_json_file(filepath, data)
    return len(data)


if __name__ == "__main__":
    data = {"users": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]}
    print("Compact:", to_json_string(data))
    print("\nPretty:")
    print(to_json_string(data, pretty=True))
    path = "/tmp/test_output.json"
    write_json_file(path, data)
    print(f"\nWritten to {path}")
    with open(path) as f:
        print(f"Read back: {json.load(f)}")
    os.unlink(path)
