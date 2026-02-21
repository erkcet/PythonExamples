"""Check if a number is a power of two using bitwise operations."""


def is_power_of_two(n: int) -> bool:
    """Return True if n is a power of two.

    A power of two has exactly one bit set: n & (n-1) == 0.
    """
    return n > 0 and (n & (n - 1)) == 0


def next_power_of_two(n: int) -> int:
    """Return the smallest power of two >= n."""
    if n <= 1:
        return 1
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1


def highest_bit(n: int) -> int:
    """Return the position of the highest set bit (0-indexed)."""
    if n <= 0:
        return -1
    return n.bit_length() - 1


if __name__ == "__main__":
    for num in [0, 1, 2, 3, 4, 16, 31, 32, 64, 100]:
        is_pow = is_power_of_two(num)
        nxt = next_power_of_two(num)
        print(f"{num:>4}: power of 2? {str(is_pow):<5}  next={nxt}")
