"""Infinite sequence generators with controlled consumption."""

import itertools


def natural_numbers(start=1):
    """Yield natural numbers starting from start, forever."""
    n = start
    while True:
        yield n
        n += 1


def cycle_items(items):
    """Yield items in a cycle, repeating forever."""
    while True:
        yield from items


def powers_of(base):
    """Yield successive powers: base^0, base^1, base^2, ..."""
    exponent = 0
    while True:
        yield base ** exponent
        exponent += 1


def take(n, iterable):
    """Take the first n items from any iterable."""
    return list(itertools.islice(iterable, n))


if __name__ == "__main__":
    print(f"First 5 naturals: {take(5, natural_numbers())}")
    print(f"Cycle 7 from [A,B,C]: {take(7, cycle_items(['A', 'B', 'C']))}")
    print(f"First 8 powers of 2: {take(8, powers_of(2))}")

    # Combine infinite generators
    paired = zip(natural_numbers(), powers_of(3))
    print(f"Paired (first 5): {take(5, paired)}")
