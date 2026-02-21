"""Swap two numbers without a temporary variable."""


def swap_xor(a: int, b: int) -> tuple[int, int]:
    """Swap using XOR (works for integers only)."""
    a ^= b
    b ^= a
    a ^= b
    return a, b


def swap_arithmetic(a: int, b: int) -> tuple[int, int]:
    """Swap using addition and subtraction."""
    a = a + b
    b = a - b
    a = a - b
    return a, b


def swap_pythonic(a, b):
    """Swap using Python tuple unpacking (the idiomatic way)."""
    return b, a


if __name__ == "__main__":
    x, y = 42, 17
    print(f"Original:    x={x}, y={y}")
    a, b = swap_xor(x, y)
    print(f"XOR swap:    x={a}, y={b}")
    a, b = swap_arithmetic(x, y)
    print(f"Arith swap:  x={a}, y={b}")
    a, b = swap_pythonic(x, y)
    print(f"Pythonic:    x={a}, y={b}")
