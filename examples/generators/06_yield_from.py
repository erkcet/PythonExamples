"""yield from for delegating to sub-generators."""


def flatten(nested):
    """Recursively flatten nested iterables using yield from."""
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


def chain(*iterables):
    """Yield all items from each iterable in sequence."""
    for it in iterables:
        yield from it


def tree_leaves(tree):
    """Yield leaf values from a dict-based tree structure."""
    if isinstance(tree, dict):
        for subtree in tree.values():
            yield from tree_leaves(subtree)
    else:
        yield tree


if __name__ == "__main__":
    nested = [1, [2, 3, [4, 5]], [6, [7]], 8]
    print(f"Flattened: {list(flatten(nested))}")

    chained = list(chain([1, 2], [3, 4], [5]))
    print(f"Chained: {chained}")

    tree = {"a": {"b": 1, "c": 2}, "d": {"e": {"f": 3}}, "g": 4}
    print(f"Leaves: {list(tree_leaves(tree))}")
