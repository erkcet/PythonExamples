"""Copy, move, and delete files and directories."""

import shutil
import tempfile
import os
from pathlib import Path


def demo_copy(base):
    """Demonstrate file copying."""
    src = os.path.join(base, "original.txt")
    Path(src).write_text("original content")
    dst = os.path.join(base, "copy.txt")
    shutil.copy2(src, dst)
    print(f"Copied: {Path(dst).read_text()}")


def demo_move(base):
    """Demonstrate file moving/renaming."""
    src = os.path.join(base, "old_name.txt")
    dst = os.path.join(base, "new_name.txt")
    Path(src).write_text("moveable")
    shutil.move(src, dst)
    print(f"Moved: exists old={os.path.exists(src)}, new={os.path.exists(dst)}")


def demo_delete(base):
    """Demonstrate file and directory deletion."""
    filepath = os.path.join(base, "temp.txt")
    Path(filepath).write_text("delete me")
    os.remove(filepath)
    print(f"File deleted: exists={os.path.exists(filepath)}")
    dirpath = os.path.join(base, "subdir")
    os.makedirs(os.path.join(dirpath, "nested"))
    shutil.rmtree(dirpath)
    print(f"Dir deleted: exists={os.path.exists(dirpath)}")


def demo_copy_tree(base):
    """Copy an entire directory tree."""
    src = os.path.join(base, "project")
    os.makedirs(os.path.join(src, "lib"))
    Path(os.path.join(src, "lib", "mod.py")).write_text("# module")
    dst = os.path.join(base, "project_backup")
    shutil.copytree(src, dst)
    print(f"Tree copied: {os.listdir(dst)}")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        demo_copy(tmpdir)
        demo_move(tmpdir)
        demo_delete(tmpdir)
        demo_copy_tree(tmpdir)
