"""Set, clear, and toggle bits."""


def set_bit(number: int, n: int) -> int:
    """Set the nth bit to 1."""
    return number | (1 << n)


def clear_bit(number: int, n: int) -> int:
    """Clear the nth bit to 0."""
    return number & ~(1 << n)


def toggle_bit(number: int, n: int) -> int:
    """Toggle the nth bit."""
    return number ^ (1 << n)


def modify_bit(number: int, n: int, value: int) -> int:
    """Set the nth bit to the given value (0 or 1)."""
    mask = ~(1 << n)
    return (number & mask) | (value << n)


if __name__ == "__main__":
    num = 0b10100000  # 160
    print(f"Original:  {num:08b} ({num})")
    s = set_bit(num, 2)
    print(f"Set bit 2: {s:08b} ({s})")
    c = clear_bit(num, 5)
    print(f"Clr bit 5: {c:08b} ({c})")
    t = toggle_bit(num, 7)
    print(f"Tog bit 7: {t:08b} ({t})")
    m = modify_bit(num, 3, 1)
    print(f"Mod bit 3: {m:08b} ({m})")
