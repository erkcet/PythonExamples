"""itertools.count, cycle, and repeat for infinite iterators."""

import itertools


def counted_items(items):
    """Number items starting from 1 using count."""
    return list(zip(itertools.count(1), items))


def round_robin(players, rounds):
    """Assign turns in round-robin fashion using cycle."""
    cycler = itertools.cycle(players)
    return [next(cycler) for _ in range(len(players) * rounds)]


def repeat_value(value, times):
    """Create a list of repeated values."""
    return list(itertools.repeat(value, times))


def initialize_grid(rows, cols, default=0):
    """Create a grid initialized with a default value using repeat."""
    return [list(itertools.repeat(default, cols)) for _ in range(rows)]


if __name__ == "__main__":
    fruits = ["apple", "banana", "cherry"]
    print("Counted:", counted_items(fruits))

    # count with step
    evens = list(itertools.islice(itertools.count(0, 2), 6))
    print("Evens:", evens)

    print("Round robin:", round_robin(["A", "B", "C"], 2))
    print("Repeat:", repeat_value("x", 4))
    print("Grid:", initialize_grid(2, 3, "."))
