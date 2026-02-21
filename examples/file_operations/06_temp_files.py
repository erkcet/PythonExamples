"""Temporary files and directories."""

import tempfile
import os


def use_named_temp_file():
    """Create a named temporary file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("temporary content\n")
        path = f.name
    print(f"Temp file: {path}")
    print(f"Content: {open(path).read().strip()}")
    os.unlink(path)
    print("Temp file cleaned up")


def use_temp_directory():
    """Create a temporary directory."""
    with tempfile.TemporaryDirectory(prefix="demo_") as tmpdir:
        print(f"Temp dir: {tmpdir}")
        filepath = os.path.join(tmpdir, "test.txt")
        with open(filepath, "w") as f:
            f.write("hello")
        print(f"File exists: {os.path.exists(filepath)}")
    print(f"Dir exists after exit: {os.path.exists(tmpdir)}")


def use_spooled_temp():
    """Use SpooledTemporaryFile (stays in memory up to max_size)."""
    with tempfile.SpooledTemporaryFile(max_size=1024, mode="w+") as f:
        f.write("small data in memory")
        f.seek(0)
        print(f"Spooled content: {f.read()}")


if __name__ == "__main__":
    use_named_temp_file()
    print("-" * 40)
    use_temp_directory()
    print("-" * 40)
    use_spooled_temp()
