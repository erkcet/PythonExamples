"""Print binary representation of integers."""


def to_binary(n: int, width: int = 0) -> str:
    """Convert integer to binary string with optional zero-padding."""
    if n < 0:
        if width:
            return format(n & ((1 << width) - 1), f"0{width}b")
        return "-" + bin(-n)[2:]
    return format(n, f"0{max(width, 1)}b")


def to_binary_groups(n: int, width: int = 32, group: int = 4) -> str:
    """Format binary with space-separated groups."""
    bits = to_binary(n, width)
    return " ".join(bits[i:i + group] for i in range(0, len(bits), group))


def binary_table(start: int, end: int) -> None:
    """Print a table of decimal, hex, octal, and binary values."""
    print(f"{'Dec':>5} {'Hex':>5} {'Oct':>5} {'Binary':>10}")
    print("-" * 28)
    for i in range(start, end + 1):
        print(f"{i:>5} {i:>5x} {i:>5o} {i:>10b}")


if __name__ == "__main__":
    binary_table(0, 16)
    print(f"\n255 grouped: {to_binary_groups(255, 16)}")
    print(f" -1 as 8-bit: {to_binary(-1, 8)}")
