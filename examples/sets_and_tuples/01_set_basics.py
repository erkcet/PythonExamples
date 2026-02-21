"""Set creation and basic operations."""


def create_sets():
    """Demonstrate various ways to create sets."""
    from_literal = {1, 2, 3, 4, 5}
    from_list = set([3, 1, 4, 1, 5, 9])
    from_string = set("hello")
    from_range = set(range(5))
    empty = set()
    return from_literal, from_list, from_string, from_range, empty


def basic_operations():
    """Show add, remove, discard, pop, and membership."""
    s = {1, 2, 3}
    s.add(4)
    s.discard(2)
    s.discard(99)  # no error if missing
    contains = 3 in s
    length = len(s)
    return s, contains, length


def set_iteration(s):
    """Iterate and filter a set."""
    evens = {x for x in s if x % 2 == 0}
    return sorted(evens)


if __name__ == "__main__":
    names = ["literal", "from_list", "from_string", "from_range", "empty"]
    for name, s in zip(names, create_sets()):
        print(f"{name}: {s}")
    s, contains, length = basic_operations()
    print(f"After ops: {s}, contains 3: {contains}, len: {length}")
    print(f"Evens in {{1..10}}: {set_iteration(set(range(1, 11)))}")
