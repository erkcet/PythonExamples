"""Using tuples as dictionary keys for multi-dimensional mappings."""


def coordinate_grid():
    """Map (x, y) coordinates to values."""
    grid = {}
    for x in range(3):
        for y in range(3):
            grid[(x, y)] = x * 3 + y + 1
    return grid


def memoize_with_tuple_keys():
    """Use tuple keys for memoization of multi-arg functions."""
    cache = {}

    def binomial(n, k):
        if k == 0 or k == n:
            return 1
        if (n, k) in cache:
            return cache[(n, k)]
        cache[(n, k)] = binomial(n - 1, k - 1) + binomial(n - 1, k)
        return cache[(n, k)]

    return binomial


def sparse_lookup(entries):
    """Build a sparse lookup table with (row, col) keys."""
    table = {(r, c): v for r, c, v in entries}
    return table


if __name__ == "__main__":
    grid = coordinate_grid()
    print(f"Grid (1,2): {grid[(1, 2)]}")
    print(f"All: {grid}")
    binom = memoize_with_tuple_keys()
    print(f"C(10,3) = {binom(10, 3)}")
    entries = [(0, 0, 1), (1, 2, 5), (3, 3, 9)]
    table = sparse_lookup(entries)
    print(f"Sparse (1,2): {table.get((1, 2), 0)}")
    print(f"Sparse (2,2): {table.get((2, 2), 0)}")
