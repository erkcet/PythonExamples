"""Flatten any nested structure (lists, tuples, etc.)."""

from collections.abc import Iterable


def flatten(nested, depth=-1):
    """Flatten a nested iterable to the given depth (-1 for unlimited)."""
    for item in nested:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)) and depth != 0:
            yield from flatten(item, depth - 1 if depth > 0 else -1)
        else:
            yield item


def flatten_dict(d, parent_key="", sep="."):
    """Flatten a nested dictionary with dot-separated keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


if __name__ == "__main__":
    nested = [1, [2, [3, 4], 5], [6, [7, [8]]]]
    print(f"Nested:    {nested}")
    print(f"Flat:      {list(flatten(nested))}")
    print(f"Depth=1:   {list(flatten(nested, depth=1))}")
    d = {"a": 1, "b": {"c": 2, "d": {"e": 3}}, "f": 4}
    print(f"\nNested dict: {d}")
    print(f"Flat dict:   {flatten_dict(d)}")
