"""Add two binary numbers represented as strings."""


def add_binary(a, b):
    """Return the sum of two binary strings as a binary string."""
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))
        carry = total // 2
    return ''.join(reversed(result))


if __name__ == "__main__":
    pairs = [("11", "1"), ("1010", "1011"), ("0", "0"), ("111", "111")]
    for a, b in pairs:
        s = add_binary(a, b)
        print(f"{a} + {b} = {s}  (decimal: {int(a,2)} + {int(b,2)} = {int(s,2)})")
