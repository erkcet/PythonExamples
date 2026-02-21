"""Searching files by pattern using glob."""

from pathlib import Path
import tempfile
import os


def setup_demo_files(base):
    """Create demo files for searching."""
    for name in ["readme.md", "setup.py", "main.py", "data.csv"]:
        (base / name).write_text(f"# {name}")
    sub = base / "sub"
    sub.mkdir()
    (sub / "helper.py").write_text("# helper")
    (sub / "notes.md").write_text("# notes")


def glob_search(directory, pattern):
    """Search for files matching a glob pattern."""
    path = Path(directory)
    matches = sorted(path.glob(pattern))
    print(f"Pattern '{pattern}': {[m.name for m in matches]}")
    return matches


def recursive_search(directory, pattern):
    """Recursively search using '**' glob."""
    path = Path(directory)
    matches = sorted(path.rglob(pattern))
    print(f"Recursive '{pattern}': {[str(m.relative_to(path)) for m in matches]}")
    return matches


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        setup_demo_files(base)
        glob_search(base, "*.py")
        glob_search(base, "*.md")
        recursive_search(base, "*.py")
        recursive_search(base, "*.md")
