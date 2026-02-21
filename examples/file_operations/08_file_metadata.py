"""File size, dates, and permissions."""

import os
import stat
import time
import tempfile


def show_file_metadata(path):
    """Display metadata for a file."""
    st = os.stat(path)
    print(f"File: {path}")
    print(f"  Size: {st.st_size} bytes")
    print(f"  Modified: {time.ctime(st.st_mtime)}")
    print(f"  Created:  {time.ctime(st.st_ctime)}")
    print(f"  Mode: {oct(st.st_mode)}")


def check_permissions(path):
    """Check read/write/execute permissions."""
    print(f"Permissions for {path}:")
    print(f"  Readable:   {os.access(path, os.R_OK)}")
    print(f"  Writable:   {os.access(path, os.W_OK)}")
    print(f"  Executable: {os.access(path, os.X_OK)}")


def format_size(size_bytes):
    """Format bytes into human-readable size."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


if __name__ == "__main__":
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Hello, metadata!\n" * 100)
        path = f.name
    show_file_metadata(path)
    check_permissions(path)
    size = os.path.getsize(path)
    print(f"Human-readable size: {format_size(size)}")
    os.remove(path)
