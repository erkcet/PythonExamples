"""Common os.path operations for file path manipulation."""

import os.path


def path_info(filepath):
    """Get detailed information about a file path."""
    return {
        "dirname": os.path.dirname(filepath),
        "basename": os.path.basename(filepath),
        "stem": os.path.splitext(os.path.basename(filepath))[0],
        "extension": os.path.splitext(filepath)[1],
        "absolute": os.path.abspath(filepath),
        "normalized": os.path.normpath(filepath),
    }


def safe_join(*parts):
    """Safely join path components."""
    return os.path.normpath(os.path.join(*parts))


def common_ancestor(paths):
    """Find the common ancestor directory of multiple paths."""
    return os.path.commonpath(paths)


def expand_user_path(path):
    """Expand ~ and environment variables in a path."""
    return os.path.expandvars(os.path.expanduser(path))


if __name__ == "__main__":
    test = "/home/user/docs/../projects/app/main.py"
    print("Path info:")
    for k, v in path_info(test).items():
        print(f"  {k}: {v}")
    print(f"Joined: {safe_join('/home', 'user', 'docs', 'file.txt')}")
    paths = ["/home/user/a/b", "/home/user/a/c", "/home/user/a"]
    print(f"Common ancestor: {common_ancestor(paths)}")
    print(f"Expanded: {expand_user_path('~/projects')}")
