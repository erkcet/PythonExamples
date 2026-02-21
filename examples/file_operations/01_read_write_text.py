"""Read and write text files."""

import tempfile
import os


def write_text(path, content):
    """Write text content to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {len(content)} chars to {path}")


def read_text(path):
    """Read entire text file and return contents."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def append_text(path, content):
    """Append text to an existing file."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    filepath = os.path.join(tempfile.gettempdir(), "demo_text.txt")
    write_text(filepath, "Hello, World!\n")
    append_text(filepath, "Second line.\n")
    content = read_text(filepath)
    print(f"File content:\n{content}")
    os.remove(filepath)
    print("Cleaned up temp file")
