"""Useful features of the sys module."""

import sys


def get_sys_info():
    """Get useful sys module information."""
    return {
        "version": sys.version,
        "platform": sys.platform,
        "executable": sys.executable,
        "path_count": len(sys.path),
        "max_int": sys.maxsize,
        "recursion_limit": sys.getrecursionlimit(),
        "byte_order": sys.byteorder,
        "default_encoding": sys.getdefaultencoding(),
    }


def get_object_size(obj):
    """Get the size of an object in bytes."""
    return sys.getsizeof(obj)


def show_size_comparison():
    """Compare memory sizes of different types."""
    objects = {
        "int(0)": 0, "int(1M)": 1_000_000, "float": 3.14,
        "str('')": "", "str('hello')": "hello",
        "list([])": [], "list([1,2,3])": [1, 2, 3],
        "dict({})": {}, "tuple(())": (),
    }
    return {k: f"{get_object_size(v)} bytes" for k, v in objects.items()}


if __name__ == "__main__":
    print("System info:")
    for k, v in get_sys_info().items():
        print(f"  {k}: {v}")
    print("\nObject sizes:")
    for k, v in show_size_comparison().items():
        print(f"  {k}: {v}")
    print(f"\nFirst 3 sys.path entries:")
    for p in sys.path[:3]:
        print(f"  {p}")
