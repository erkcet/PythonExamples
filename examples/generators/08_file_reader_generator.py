"""Reading files lazily using generators for memory efficiency."""

import tempfile
import os


def read_lines(filepath):
    """Yield lines from a file one at a time."""
    with open(filepath, "r") as f:
        for line in f:
            yield line.rstrip("\n")


def grep(pattern, lines):
    """Yield lines that contain the given pattern."""
    for line in lines:
        if pattern in line:
            yield line


def numbered(lines):
    """Yield (line_number, line) tuples starting from 1."""
    for i, line in enumerate(lines, 1):
        yield i, line


if __name__ == "__main__":
    # Create a temp file for demonstration
    content = "apple\nbanana\ncherry\napricot\nblueberry\navocado\n"
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    tmp.write(content)
    tmp.close()

    try:
        # Pipeline: read -> grep -> number
        pipeline = numbered(grep("a", read_lines(tmp.name)))
        for num, line in pipeline:
            print(f"  Line {num}: {line}")
    finally:
        os.unlink(tmp.name)
