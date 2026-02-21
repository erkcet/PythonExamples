"""Basic bitwise operations: AND, OR, XOR, NOT, shifts."""


def demonstrate_operations(a: int, b: int) -> dict[str, int]:
    """Perform all basic bitwise operations on a and b."""
    return {
        "AND": a & b,
        "OR": a | b,
        "XOR": a ^ b,
        "NOT a": ~a,
        "a << 1": a << 1,
        "a >> 1": a >> 1,
    }


def show_binary(label: str, value: int, width: int = 8) -> str:
    """Format an integer with its binary representation."""
    return f"{label:>8} = {value:>4} = {value & ((1 << width) - 1):0{width}b}"


if __name__ == "__main__":
    a, b = 0b1100, 0b1010
    print(show_binary("a", a))
    print(show_binary("b", b))
    print("-" * 30)
    ops = demonstrate_operations(a, b)
    for name, val in ops.items():
        print(show_binary(name, val))
