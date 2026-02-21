"""Reading and writing CSV files."""

import csv
import tempfile
import os


def write_csv(path, headers, rows):
    """Write rows to a CSV file with headers."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {path}")


def read_csv(path):
    """Read CSV file and return list of dicts."""
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_dict_csv(path, data):
    """Write list of dicts as CSV."""
    if not data:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    filepath = os.path.join(tempfile.gettempdir(), "demo.csv")
    headers = ["name", "age", "city"]
    rows = [["Alice", 30, "NYC"], ["Bob", 25, "LA"]]
    write_csv(filepath, headers, rows)
    records = read_csv(filepath)
    for r in records:
        print(f"  {r['name']}, age {r['age']}, from {r['city']}")
    os.remove(filepath)
