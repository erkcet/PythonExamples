"""Transform data between JSON and CSV formats."""

import json
import csv
import io


def json_to_csv(json_data):
    """Convert a list of JSON objects to CSV string."""
    if not json_data:
        return ""
    headers = list(json_data[0].keys())
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()
    writer.writerows(json_data)
    return output.getvalue()


def csv_to_json(csv_text):
    """Convert CSV string to list of JSON objects."""
    reader = csv.DictReader(io.StringIO(csv_text))
    return [dict(row) for row in reader]


def flatten_json_for_csv(data, prefix=""):
    """Flatten nested JSON for CSV export."""
    items = {}
    for k, v in data.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            items.update(flatten_json_for_csv(v, key))
        else:
            items[key] = v
    return items


if __name__ == "__main__":
    json_data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    csv_output = json_to_csv(json_data)
    print(f"JSON -> CSV:\n{csv_output}")
    back = csv_to_json(csv_output)
    print(f"CSV -> JSON: {json.dumps(back, indent=2)}")
    nested = {"user": {"name": "Alice", "addr": {"city": "NYC"}}, "active": True}
    print(f"\nFlattened: {flatten_json_for_csv(nested)}")
