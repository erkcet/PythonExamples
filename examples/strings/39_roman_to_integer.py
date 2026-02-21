"""Convert a Roman numeral string to an integer."""


def roman_to_int(s):
    """Convert Roman numeral to integer."""
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            result -= values[s[i]]
        else:
            result += values[s[i]]
    return result


if __name__ == "__main__":
    numerals = ["III", "IV", "IX", "XLII", "MCMXCIV", "MMXXIV", "DCCCXC"]
    for r in numerals:
        print(f"{r:12s} = {roman_to_int(r)}")
