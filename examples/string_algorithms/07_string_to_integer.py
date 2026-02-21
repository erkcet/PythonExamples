"""String to integer (atoi) implementation."""


def my_atoi(s):
    """Convert string to 32-bit signed integer (LeetCode-style atoi)."""
    s = s.strip()
    if not s:
        return 0
    sign = 1
    idx = 0
    if s[idx] in ("+", "-"):
        sign = -1 if s[idx] == "-" else 1
        idx += 1
    result = 0
    while idx < len(s) and s[idx].isdigit():
        result = result * 10 + int(s[idx])
        idx += 1
    result *= sign
    INT_MIN, INT_MAX = -(2 ** 31), 2 ** 31 - 1
    return max(INT_MIN, min(result, INT_MAX))


def safe_int(s, default=0):
    """Safely convert string to int with a default value."""
    try:
        return int(s.strip())
    except (ValueError, AttributeError):
        return default


def parse_number(s):
    """Parse various number formats from strings."""
    s = s.strip().lower()
    if s.startswith("0x"):
        return int(s, 16)
    if s.startswith("0b"):
        return int(s, 2)
    if s.startswith("0o"):
        return int(s, 8)
    return int(float(s))


if __name__ == "__main__":
    tests = ["42", "   -42", "4193 with words", "words 987", "", "2147483648"]
    for t in tests:
        print(f"  atoi('{t}') = {my_atoi(t)}")
    print(f"\nparse_number('0xff') = {parse_number('0xff')}")
    print(f"parse_number('0b1010') = {parse_number('0b1010')}")
    print(f"safe_int('nope') = {safe_int('nope', -1)}")
