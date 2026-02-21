"""Read CSV files using the csv module."""

import csv
import io


def read_csv_string(csv_text):
    """Parse CSV from a string."""
    reader = csv.reader(io.StringIO(csv_text))
    return list(reader)


def read_csv_file(filepath, delimiter=","):
    """Read a CSV file and return rows as lists."""
    with open(filepath, "r", newline="") as f:
        return list(csv.reader(f, delimiter=delimiter))


def csv_to_dicts(csv_text):
    """Parse CSV into list of dictionaries using first row as headers."""
    reader = csv.DictReader(io.StringIO(csv_text))
    return list(reader)


def filter_csv(csv_text, predicate):
    """Filter CSV rows by a predicate on the dict representation."""
    rows = csv_to_dicts(csv_text)
    return [r for r in rows if predicate(r)]


if __name__ == "__main__":
    csv_data = "name,age,city\nAlice,30,NYC\nBob,25,LA\nCharlie,35,Chicago"
    print("Raw rows:", read_csv_string(csv_data))
    print("\nAs dicts:")
    for row in csv_to_dicts(csv_data):
        print(f"  {row}")
    older = filter_csv(csv_data, lambda r: int(r["age"]) >= 30)
    print(f"\nAge >= 30: {older}")
