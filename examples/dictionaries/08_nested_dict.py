"""Working with nested dictionaries."""


def get_nested(d, *keys, default=None):
    """Safely access a deeply nested value."""
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key, default)
        else:
            return default
    return d


def set_nested(d, keys, value):
    """Set a value in a nested dict, creating intermediate dicts."""
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value


def flatten_nested(d, parent_key="", sep="."):
    """Flatten a nested dict to dot-notation keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_nested(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def unflatten(d, sep="."):
    """Unflatten dot-notation keys back to nested dict."""
    result = {}
    for key, val in d.items():
        set_nested(result, key.split(sep), val)
    return result


if __name__ == "__main__":
    config = {"db": {"host": "localhost", "credentials": {"user": "admin", "pass": "secret"}}}
    print(f"Nested get: {get_nested(config, 'db', 'credentials', 'user')}")
    print(f"Missing: {get_nested(config, 'db', 'port', default=5432)}")
    print(f"Flattened: {flatten_nested(config)}")
    flat = {"a.b.c": 1, "a.b.d": 2, "a.e": 3}
    print(f"Unflattened: {unflatten(flat)}")
