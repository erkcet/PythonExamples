"""Temporary directory context manager."""

import os
import shutil
import tempfile
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def working_directory(base_prefix="work_"):
    """Create a temp working directory and clean up on exit."""
    tmpdir = tempfile.mkdtemp(prefix=base_prefix)
    print(f"Created working dir: {tmpdir}")
    try:
        yield Path(tmpdir)
    finally:
        shutil.rmtree(tmpdir)
        print(f"Cleaned up: {tmpdir}")


@contextmanager
def project_scaffold(name):
    """Create a project scaffold in a temp directory."""
    with working_directory(f"{name}_") as base:
        for subdir in ["src", "tests", "docs"]:
            (base / subdir).mkdir()
        (base / "README.md").write_text(f"# {name}\n")
        yield base


if __name__ == "__main__":
    with working_directory() as wd:
        file_path = wd / "data.txt"
        file_path.write_text("temporary data")
        print(f"File exists: {file_path.exists()}")
        print(f"Content: {file_path.read_text()}")

    print("\n--- Project scaffold ---")
    with project_scaffold("myproject") as proj:
        contents = sorted(p.name for p in proj.iterdir())
        print(f"Scaffold contents: {contents}")
    print("All cleaned up")
