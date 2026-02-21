"""Process large files line by line efficiently."""

import tempfile
import os


def generate_large_file(path, lines=1000):
    """Generate a test file with numbered lines."""
    with open(path, "w") as f:
        for i in range(lines):
            f.write(f"Line {i:04d}: {'x' * 50}\n")
    print(f"Generated {lines} lines in {path}")


def count_matching_lines(path, keyword):
    """Count lines containing a keyword without loading entire file."""
    count = 0
    with open(path, "r") as f:
        for line in f:
            if keyword in line:
                count += 1
    return count


def head(path, n=5):
    """Read the first N lines of a file."""
    lines = []
    with open(path, "r") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line.rstrip())
    return lines


def transform_file(src, dst, func):
    """Transform a file line by line."""
    count = 0
    with open(src, "r") as fin, open(dst, "w") as fout:
        for line in fin:
            fout.write(func(line))
            count += 1
    return count


if __name__ == "__main__":
    filepath = os.path.join(tempfile.gettempdir(), "large_demo.txt")
    generate_large_file(filepath)
    matches = count_matching_lines(filepath, "Line 05")
    print(f"Lines matching 'Line 05': {matches}")
    print(f"First 3 lines: {head(filepath, 3)}")
    outpath = filepath + ".upper"
    n = transform_file(filepath, outpath, str.upper)
    print(f"Transformed {n} lines")
    os.remove(filepath)
    os.remove(outpath)
