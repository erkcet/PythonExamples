"""Calculate the Hamming distance between two strings of equal length."""


def hamming_distance(s1, s2):
    """Return the number of positions where corresponding characters differ."""
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def hamming_distance_binary(n1, n2):
    """Return the Hamming distance between two integers (in binary)."""
    xor = n1 ^ n2
    return bin(xor).count('1')


if __name__ == "__main__":
    pairs = [("karolin", "kathrin"), ("1011101", "1001001"), ("python", "pithon")]
    for a, b in pairs:
        print(f"hamming('{a}', '{b}') = {hamming_distance(a, b)}")
    print(f"\nBinary hamming(93, 73) = {hamming_distance_binary(93, 73)}")
    print(f"  93 = {bin(93)}")
    print(f"  73 = {bin(73)}")
