"""Deep merge dictionaries recursively."""


def deep_merge(base, override):
    """Recursively merge override into base, returning a new dict."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def deep_merge_many(*dicts):
    """Merge multiple dictionaries deeply, left to right."""
    result = {}
    for d in dicts:
        result = deep_merge(result, d)
    return result


def deep_update(base, override):
    """Deep merge in-place (mutates base)."""
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            deep_update(base[key], value)
        else:
            base[key] = value
    return base


if __name__ == "__main__":
    a = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    b = {"db": {"port": 3306, "name": "mydb"}, "debug": True}
    print(f"Base:     {a}")
    print(f"Override: {b}")
    print(f"Merged:   {deep_merge(a, b)}")
    c = {"db": {"ssl": True}}
    print(f"Three-way: {deep_merge_many(a, b, c)}")
