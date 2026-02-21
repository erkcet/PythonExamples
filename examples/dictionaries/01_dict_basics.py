"""Dictionary basics: creation, access, and modification."""


def create_dicts():
    """Various ways to create dictionaries."""
    literal = {"name": "Alice", "age": 30}
    from_tuples = dict([("a", 1), ("b", 2)])
    from_keys = dict.fromkeys(["x", "y", "z"], 0)
    from_zip = dict(zip("abc", [1, 2, 3]))
    return literal, from_tuples, from_keys, from_zip


def access_patterns(d):
    """Demonstrate safe and unsafe access."""
    direct = d["name"]
    safe = d.get("missing", "default")
    keys = list(d.keys())
    values = list(d.values())
    items = list(d.items())
    return direct, safe, keys, values, items


def modify_dict(d):
    """Show common dict mutations."""
    d = d.copy()
    d["email"] = "alice@example.com"
    d["age"] = 31
    del d["age"]
    removed = d.pop("email", None)
    return d, removed


if __name__ == "__main__":
    for name, d in zip(["literal", "tuples", "fromkeys", "zip"], create_dicts()):
        print(f"{name}: {d}")
    person = {"name": "Alice", "age": 30}
    direct, safe, keys, vals, items = access_patterns(person)
    print(f"Direct: {direct}, Safe: {safe}, Keys: {keys}")
    modified, removed = modify_dict(person)
    print(f"Modified: {modified}, Removed: {removed}")
