"""Set operations: union, intersection, difference, symmetric difference."""


def demonstrate_operations(a, b):
    """Show all four core set operations."""
    return {
        "union": a | b,
        "intersection": a & b,
        "difference_a_b": a - b,
        "difference_b_a": b - a,
        "symmetric_diff": a ^ b,
    }


def subset_superset(a, b):
    """Check subset and superset relationships."""
    return {
        "a_subset_b": a <= b,
        "a_proper_subset_b": a < b,
        "a_superset_b": a >= b,
        "disjoint": a.isdisjoint(b),
    }


def chained_operations(*sets):
    """Find elements common to all sets."""
    result = sets[0]
    for s in sets[1:]:
        result = result & s
    return result


if __name__ == "__main__":
    a, b = {1, 2, 3, 4}, {3, 4, 5, 6}
    for op, val in demonstrate_operations(a, b).items():
        print(f"{op}: {sorted(val)}")
    c = {1, 2}
    for rel, val in subset_superset(c, a).items():
        print(f"{rel}: {val}")
    print(f"Common to all: {chained_operations(a, b, {3, 4, 7})}")
