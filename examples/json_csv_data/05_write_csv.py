"""Write data to CSV files."""

import csv
import io
import os


def write_csv_file(filepath, headers, rows):
    """Write rows to a CSV file with headers."""
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def to_csv_string(headers, rows):
    """Convert data to a CSV string."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(headers)
    writer.writerows(rows)
    return output.getvalue()


def append_csv_row(filepath, row):
    """Append a single row to an existing CSV file."""
    with open(filepath, "a", newline="") as f:
        csv.writer(f).writerow(row)


if __name__ == "__main__":
    headers = ["name", "score", "grade"]
    rows = [["Alice", 95, "A"], ["Bob", 82, "B"], ["Charlie", 78, "C"]]
    csv_str = to_csv_string(headers, rows)
    print(f"CSV string:\n{csv_str}")
    path = "/tmp/test_grades.csv"
    write_csv_file(path, headers, rows)
    append_csv_row(path, ["Diana", 91, "A"])
    with open(path) as f:
        print(f"File contents:\n{f.read()}")
    os.unlink(path)
