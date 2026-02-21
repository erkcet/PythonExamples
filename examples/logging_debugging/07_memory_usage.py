"""Tracking memory usage with sys.getsizeof."""

import sys


def object_sizes():
    """Show sizes of common Python objects."""
    objects = {
        "int(0)": 0,
        "int(1000)": 1000,
        "float": 3.14,
        "str('')": "",
        "str('hello')": "hello",
        "list([])": [],
        "list(range(10))": list(range(10)),
        "dict({})": {},
        "set()": set(),
        "tuple()": (),
        "bool": True,
        "None": None,
    }
    for label, obj in objects.items():
        print(f"  {label:20s} = {sys.getsizeof(obj):>6d} bytes")


def compare_containers(n):
    """Compare memory of list vs tuple vs set."""
    data = range(n)
    containers = {
        "list": list(data),
        "tuple": tuple(data),
        "set": set(data),
    }
    for name, obj in containers.items():
        print(f"  {name}({n}): {sys.getsizeof(obj):,} bytes")


def deep_size(obj, seen=None):
    """Approximate deep size of an object."""
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    size = sys.getsizeof(obj)
    if isinstance(obj, dict):
        size += sum(deep_size(k, seen) + deep_size(v, seen) for k, v in obj.items())
    elif isinstance(obj, (list, tuple, set)):
        size += sum(deep_size(i, seen) for i in obj)
    return size


if __name__ == "__main__":
    print("=== Object sizes ===")
    object_sizes()
    print("\n=== Container comparison ===")
    compare_containers(1000)
    print("\n=== Deep size ===")
    nested = {"a": [1, 2, 3], "b": {"c": "hello"}}
    print(f"  Shallow: {sys.getsizeof(nested)} bytes")
    print(f"  Deep:    {deep_size(nested)} bytes")
