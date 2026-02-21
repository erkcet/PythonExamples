"""Create, list, and walk directories."""

import os
import tempfile
from pathlib import Path


def create_directory_tree(base):
    """Create a sample directory tree."""
    dirs = ["src", "src/utils", "tests", "docs"]
    for d in dirs:
        os.makedirs(os.path.join(base, d), exist_ok=True)
    for name in ["src/main.py", "src/utils/helpers.py", "tests/test_main.py"]:
        Path(os.path.join(base, name)).write_text(f"# {name}\n")
    print(f"Created tree under {base}")


def list_directory(path):
    """List directory contents with type indicators."""
    for entry in sorted(os.scandir(path), key=lambda e: e.name):
        kind = "DIR " if entry.is_dir() else "FILE"
        print(f"  [{kind}] {entry.name}")


def walk_tree(path):
    """Walk directory tree and print all files."""
    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}{os.path.basename(root)}/")
        for f in sorted(files):
            print(f"{indent}  {f}")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        create_directory_tree(tmpdir)
        print("\nDirectory listing:")
        list_directory(tmpdir)
        print("\nFull tree:")
        walk_tree(tmpdir)
