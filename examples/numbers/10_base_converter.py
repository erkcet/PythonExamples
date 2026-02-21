"""Convert between number bases."""

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n: int, base: int) -> str:
    """Convert a non-negative integer to the given base (2-36)."""
    if not 2 <= base <= 36:
        raise ValueError("Base must be between 2 and 36")
    if n == 0:
        return "0"
    negative = n < 0
    n = abs(n)
    result = []
    while n:
        result.append(DIGITS[n % base])
        n //= base
    if negative:
        result.append("-")
    return "".join(reversed(result))


def from_base(s: str, base: int) -> int:
    """Convert a string in the given base to an integer."""
    return int(s, base)


def convert(value: str, from_b: int, to_b: int) -> str:
    """Convert a number string from one base to another."""
    decimal = from_base(value, from_b)
    return to_base(decimal, to_b)


if __name__ == "__main__":
    num = 255
    for base in [2, 8, 10, 16]:
        print(f"{num} in base {base:>2}: {to_base(num, base)}")
    print(f"\nBinary '11010' -> decimal: {from_base('11010', 2)}")
    print(f"Hex 'FF' -> octal: {convert('FF', 16, 8)}")
