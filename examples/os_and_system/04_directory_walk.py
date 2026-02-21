"""Directory traversal using os.walk."""

import os


def walk_directory(root, max_depth=None):
    """Walk a directory tree and return file info."""
    files_found = []
    root = os.path.abspath(root)
    for dirpath, dirnames, filenames in os.walk(root):
        depth = dirpath.replace(root, "").count(os.sep)
        if max_depth is not None and depth >= max_depth:
            dirnames.clear()
            continue
        for f in filenames:
            full = os.path.join(dirpath, f)
            files_found.append({"path": full, "size": os.path.getsize(full), "depth": depth})
    return files_found


def find_by_extension(root, ext):
    """Find all files with a given extension."""
    return [f["path"] for f in walk_directory(root) if f["path"].endswith(ext)]


def directory_stats(root):
    """Get statistics about a directory tree."""
    files = walk_directory(root)
    return {
        "total_files": len(files),
        "total_size": sum(f["size"] for f in files),
        "extensions": list({os.path.splitext(f["path"])[1] for f in files}),
    }


if __name__ == "__main__":
    target = os.path.dirname(os.path.abspath(__file__))
    print(f"Walking: {target}")
    stats = directory_stats(target)
    print(f"Stats: {stats}")
    py_files = find_by_extension(target, ".py")
    print(f"Python files: {len(py_files)}")
    for f in py_files[:5]:
        print(f"  {f}")
