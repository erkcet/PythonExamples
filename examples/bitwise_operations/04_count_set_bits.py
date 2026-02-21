"""Count number of set bits (Hamming weight)."""


def count_bits_loop(n: int) -> int:
    """Count set bits by checking each bit."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def count_bits_kernighan(n: int) -> int:
    """Count set bits using Brian Kernighan's algorithm."""
    count = 0
    while n:
        n &= n - 1  # clears the lowest set bit
        count += 1
    return count


def count_bits_builtin(n: int) -> int:
    """Count set bits using Python's built-in."""
    return bin(n).count("1")


def hamming_distance(a: int, b: int) -> int:
    """Count the number of differing bits between a and b."""
    return count_bits_kernighan(a ^ b)


if __name__ == "__main__":
    for num in [0, 1, 7, 15, 128, 255]:
        c = count_bits_kernighan(num)
        print(f"{num:>4} ({num:08b}): {c} set bits")
    print(f"\nHamming distance(14, 11) = {hamming_distance(14, 11)}")
