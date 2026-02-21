"""Implement the atoi function to convert a string to a 32-bit signed integer."""


def my_atoi(s):
    """Parse a string to a 32-bit signed integer, handling edge cases."""
    s = s.strip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[i] in ('+', '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    result *= sign
    INT_MIN, INT_MAX = -(2**31), 2**31 - 1
    return max(INT_MIN, min(result, INT_MAX))


if __name__ == "__main__":
    tests = ["42", "   -42", "4193 with words", "words and 987", "", "+-12",
             "-91283472332", "2147483648"]
    for t in tests:
        print(f"atoi({repr(t):25s}) = {my_atoi(t)}")
