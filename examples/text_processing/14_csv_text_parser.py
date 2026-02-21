"""Parse CSV-formatted text handling quoted fields and commas within quotes."""

import csv
import io


def parse_csv(text, delimiter=','):
    """Parse CSV text into a list of rows (lists of strings)."""
    reader = csv.reader(io.StringIO(text), delimiter=delimiter)
    return [row for row in reader]


def to_csv(rows, delimiter=','):
    """Convert rows back to CSV text."""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=delimiter)
    writer.writerows(rows)
    return output.getvalue().strip()


if __name__ == "__main__":
    csv_text = (
        'name,age,city\n'
        '"Smith, John",30,"New York"\n'
        'Jane Doe,25,Chicago\n'
        '"O\'Brien, Pat",40,"San Francisco"'
    )
    rows = parse_csv(csv_text)
    print("Parsed CSV:")
    for row in rows:
        print(f"  {row}")
    print("\nBack to CSV:")
    print(to_csv(rows))
