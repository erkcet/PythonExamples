"""Multiply two numbers represented as strings without converting to int directly."""


def multiply_strings(num1, num2):
    """Multiply two non-negative numbers given as strings."""
    if num1 == "0" or num2 == "0":
        return "0"
    n, m = len(num1), len(num2)
    result = [0] * (n + m)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            total = mul + result[p2]
            result[p2] = total % 10
            result[p1] += total // 10
    result_str = ''.join(str(d) for d in result)
    return result_str.lstrip('0') or "0"


if __name__ == "__main__":
    pairs = [("123", "456"), ("99", "99"), ("0", "12345"), ("999", "999")]
    for a, b in pairs:
        result = multiply_strings(a, b)
        print(f"{a} * {b} = {result}  (verify: {int(a) * int(b)})")
