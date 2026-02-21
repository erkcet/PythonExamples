"""pathlib.Path usage for file path manipulation."""

from pathlib import Path
import tempfile


def explore_path(filepath):
    """Show various path components."""
    p = Path(filepath)
    print(f"Path:      {p}")
    print(f"Name:      {p.name}")
    print(f"Stem:      {p.stem}")
    print(f"Suffix:    {p.suffix}")
    print(f"Parent:    {p.parent}")
    print(f"Absolute:  {p.is_absolute()}")


def build_paths():
    """Demonstrate path construction."""
    base = Path("/usr") / "local" / "bin"
    print(f"Joined: {base}")
    home = Path.home()
    print(f"Home: {home}")
    cwd = Path.cwd()
    print(f"CWD: {cwd}")
    return base


def path_operations():
    """Create and check paths."""
    tmp = Path(tempfile.gettempdir()) / "pathlib_demo"
    tmp.mkdir(exist_ok=True)
    test_file = tmp / "example.txt"
    test_file.write_text("hello from pathlib")
    print(f"Exists: {test_file.exists()}")
    print(f"Is file: {test_file.is_file()}")
    print(f"Content: {test_file.read_text()}")
    test_file.unlink()
    tmp.rmdir()


if __name__ == "__main__":
    explore_path("/home/user/docs/report.pdf")
    print("-" * 40)
    build_paths()
    print("-" * 40)
    path_operations()
