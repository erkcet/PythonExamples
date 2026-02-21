"""Binary file operations."""

import struct
import tempfile
import os


def write_binary_records(path, records):
    """Write (int, float) records in binary format."""
    with open(path, "wb") as f:
        for id_, value in records:
            f.write(struct.pack("!if", id_, value))
    print(f"Wrote {len(records)} records to {path}")


def read_binary_records(path):
    """Read binary records back as (int, float) tuples."""
    record_size = struct.calcsize("!if")
    results = []
    with open(path, "rb") as f:
        while chunk := f.read(record_size):
            results.append(struct.unpack("!if", chunk))
    return results


def write_bytes_example(path):
    """Write raw bytes to a file."""
    data = bytes(range(256))
    with open(path, "wb") as f:
        f.write(data)
    return len(data)


if __name__ == "__main__":
    rec_path = os.path.join(tempfile.gettempdir(), "records.bin")
    records = [(1, 3.14), (2, 2.72), (3, 1.41)]
    write_binary_records(rec_path, records)
    loaded = read_binary_records(rec_path)
    for id_, val in loaded:
        print(f"  Record {id_}: {val:.2f}")
    os.remove(rec_path)
