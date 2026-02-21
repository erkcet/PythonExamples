"""Basic and nested list comprehensions."""


def squares(n):
    """Squares of numbers 1 to n."""
    return [x ** 2 for x in range(1, n + 1)]


def even_squares(n):
    """Squares of even numbers only."""
    return [x ** 2 for x in range(1, n + 1) if x % 2 == 0]


def multiplication_table(rows, cols):
    """Generate a multiplication table as a nested list."""
    return [[r * c for c in range(1, cols + 1)] for r in range(1, rows + 1)]


def pairs(lst1, lst2):
    """All pairs from two lists (Cartesian product)."""
    return [(a, b) for a in lst1 for b in lst2]


if __name__ == "__main__":
    print(f"Squares(6): {squares(6)}")
    print(f"Even squares(10): {even_squares(10)}")
    print("3x4 table:")
    for row in multiplication_table(3, 4):
        print(f"  {row}")
    print(f"Pairs: {pairs([1, 2], ['a', 'b', 'c'])}")
