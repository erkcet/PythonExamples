"""Find the intersection of multiple lists."""


def intersect_two(a, b):
    """Intersection preserving order from the first list."""
    b_set = set(b)
    return [x for x in a if x in b_set]


def intersect_sets(*lists):
    """Intersection of multiple lists using set operations."""
    result = set(lists[0])
    for lst in lists[1:]:
        result &= set(lst)
    return sorted(result)


def intersect_with_count(a, b):
    """Intersection accounting for duplicates."""
    from collections import Counter
    ca, cb = Counter(a), Counter(b)
    return sorted((ca & cb).elements())


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 3]
    b = [3, 4, 5, 6, 7, 3]
    c = [5, 3, 8, 9]
    print(f"Two-list (order): {intersect_two(a, b)}")
    print(f"Multi-list:       {intersect_sets(a, b, c)}")
    print(f"With duplicates:  {intersect_with_count(a, b)}")
