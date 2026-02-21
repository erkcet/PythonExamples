"""Various bit manipulation tricks for abs, min, max, and more."""


def abs_bitwise(n: int, bits: int = 32) -> int:
    """Compute absolute value using bit manipulation (fixed-width)."""
    mask = n >> (bits - 1)
    return (n + mask) ^ mask


def is_opposite_sign(a: int, b: int) -> bool:
    """Check if two integers have opposite signs."""
    return (a ^ b) < 0


def average_no_overflow(a: int, b: int) -> int:
    """Compute floor average without overflow."""
    return (a & b) + ((a ^ b) >> 1)


def turn_off_rightmost_bit(n: int) -> int:
    """Turn off the rightmost set bit."""
    return n & (n - 1)


def isolate_rightmost_bit(n: int) -> int:
    """Isolate the rightmost set bit."""
    return n & (-n)


if __name__ == "__main__":
    print(f"abs_bitwise(-42) = {abs_bitwise(-42)}")
    print(f"opposite_sign(5, -3) = {is_opposite_sign(5, -3)}")
    print(f"average(10, 20) = {average_no_overflow(10, 20)}")
    n = 0b1010100
    print(f"\n{n:08b} -> turn off rightmost: {turn_off_rightmost_bit(n):08b}")
    print(f"{n:08b} -> isolate rightmost:  {isolate_rightmost_bit(n):08b}")
