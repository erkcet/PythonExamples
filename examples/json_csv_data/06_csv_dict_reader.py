"""DictReader and DictWriter for CSV with named fields."""

import csv
import io


def read_as_dicts(csv_text, fieldnames=None):
    """Read CSV as list of ordered dictionaries."""
    reader = csv.DictReader(io.StringIO(csv_text), fieldnames=fieldnames)
    return list(reader)


def write_dicts(records, fieldnames=None):
    """Write list of dicts to CSV string."""
    if not records:
        return ""
    fieldnames = fieldnames or list(records[0].keys())
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)
    return output.getvalue()


def transform_csv(csv_text, transform_fn):
    """Read CSV, transform each record, and write back."""
    records = read_as_dicts(csv_text)
    transformed = [transform_fn(r) for r in records]
    return write_dicts(transformed)


if __name__ == "__main__":
    csv_data = "product,price,quantity\nApple,1.20,50\nBanana,0.50,100\nCherry,3.00,25"
    records = read_as_dicts(csv_data)
    print("Records:")
    for r in records:
        print(f"  {dict(r)}")
    def add_total(r):
        r["total"] = f"{float(r['price']) * int(r['quantity']):.2f}"
        return r
    result = transform_csv(csv_data, add_total)
    print(f"\nWith totals:\n{result}")
