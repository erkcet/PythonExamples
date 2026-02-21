"""Josephus problem: find the survivor position."""


def josephus(n, k):
    """Find the survivor position (0-indexed) for n people, every k-th eliminated."""
    if n == 1:
        return 0
    return (josephus(n - 1, k) + k) % n


def josephus_iterative(n, k):
    """Iterative solution for the Josephus problem."""
    pos = 0
    for i in range(2, n + 1):
        pos = (pos + k) % i
    return pos


def josephus_sequence(n, k):
    """Return the full elimination order."""
    circle = list(range(n))
    order = []
    idx = 0
    while circle:
        idx = (idx + k - 1) % len(circle)
        order.append(circle.pop(idx))
        if idx == len(circle):
            idx = 0
    return order


if __name__ == "__main__":
    n, k = 10, 3
    print(f"Josephus({n}, {k})")
    print(f"  Survivor (recursive):  position {josephus(n, k)}")
    print(f"  Survivor (iterative):  position {josephus_iterative(n, k)}")
    seq = josephus_sequence(n, k)
    print(f"  Elimination order: {seq}")
    print(f"  Last standing: {seq[-1]}")
