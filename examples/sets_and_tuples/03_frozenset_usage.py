"""Frozenset as immutable set: usable as dict key or set member."""


def frozenset_as_key():
    """Use frozensets as dictionary keys for edge-pair lookups."""
    edge_weights = {
        frozenset({"A", "B"}): 5,
        frozenset({"B", "C"}): 3,
        frozenset({"A", "C"}): 7,
    }
    return edge_weights


def set_of_sets():
    """Create a set of frozensets (set of sets)."""
    groups = {
        frozenset({1, 2, 3}),
        frozenset({4, 5}),
        frozenset({1, 2, 3}),  # duplicate, will be removed
    }
    return groups


def frozenset_operations():
    """Frozensets support the same read-only operations as sets."""
    a = frozenset([1, 2, 3])
    b = frozenset([3, 4, 5])
    return a | b, a & b, a - b


if __name__ == "__main__":
    weights = frozenset_as_key()
    print(f"A-B weight: {weights[frozenset({'A', 'B'})]}")
    print(f"B-A weight: {weights[frozenset({'B', 'A'})]}")  # same key
    print(f"Set of sets: {set_of_sets()}")
    u, i, d = frozenset_operations()
    print(f"Union: {u}, Inter: {i}, Diff: {d}")
