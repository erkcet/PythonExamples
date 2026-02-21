"""Merging dictionaries using multiple approaches."""


def merge_unpack(d1, d2):
    """Merge using dictionary unpacking (Python 3.5+)."""
    return {**d1, **d2}


def merge_pipe(d1, d2):
    """Merge using the | operator (Python 3.9+)."""
    return d1 | d2


def merge_update(d1, d2):
    """Merge using update (modifies a copy)."""
    result = d1.copy()
    result.update(d2)
    return result


def deep_merge(d1, d2):
    """Recursively merge nested dictionaries."""
    result = d1.copy()
    for key, val in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = deep_merge(result[key], val)
        else:
            result[key] = val
    return result


if __name__ == "__main__":
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    print(f"Unpack: {merge_unpack(a, b)}")
    print(f"Pipe:   {merge_pipe(a, b)}")
    print(f"Update: {merge_update(a, b)}")
    nested1 = {"db": {"host": "localhost", "port": 5432}, "debug": True}
    nested2 = {"db": {"port": 3306, "name": "mydb"}, "version": 2}
    print(f"Deep:   {deep_merge(nested1, nested2)}")
