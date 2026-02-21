"""Check if the nth bit is set."""


def is_bit_set(number: int, n: int) -> bool:
    """Return True if the nth bit (0-indexed from right) is set."""
    return bool(number & (1 << n))


def get_bit(number: int, n: int) -> int:
    """Return the value of the nth bit (0 or 1)."""
    return (number >> n) & 1


def get_all_bits(number: int, width: int = 8) -> list[int]:
    """Return a list of all bit values from MSB to LSB."""
    return [get_bit(number, i) for i in range(width - 1, -1, -1)]


if __name__ == "__main__":
    num = 0b10110101  # 181
    print(f"Number: {num} (binary: {num:08b})")
    print(f"Bits: {get_all_bits(num)}")
    print()
    for i in range(8):
        status = "SET" if is_bit_set(num, i) else "not set"
        print(f"  Bit {i}: {status}")
