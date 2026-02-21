"""Common dict methods: get, setdefault, update, pop."""


def safe_access(d, key, default=None):
    """Use get() for safe key access."""
    return d.get(key, default)


def count_with_setdefault(words):
    """Use setdefault to build a word-to-indices mapping."""
    index = {}
    for i, word in enumerate(words):
        index.setdefault(word, []).append(i)
    return index


def merge_with_update(base, *others):
    """Merge dicts using update (last wins)."""
    result = base.copy()
    for other in others:
        result.update(other)
    return result


def pop_with_default(d, keys):
    """Pop multiple keys safely, collecting removed values."""
    return {k: d.pop(k, None) for k in keys}


if __name__ == "__main__":
    d = {"a": 1, "b": 2}
    print(f"get('c', 0): {safe_access(d, 'c', 0)}")
    words = ["the", "cat", "sat", "on", "the", "mat", "the"]
    print(f"Word indices: {count_with_setdefault(words)}")
    base = {"a": 1, "b": 2}
    print(f"Merged: {merge_with_update(base, {'b': 3, 'c': 4})}")
    data = {"x": 10, "y": 20, "z": 30}
    removed = pop_with_default(data, ["y", "w"])
    print(f"Popped: {removed}, remaining: {data}")
