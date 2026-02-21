"""Convert between roman numerals and integers."""

ROMAN_MAP = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]
ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M": 1000}


def int_to_roman(n: int) -> str:
    """Convert an integer (1-3999) to a Roman numeral string."""
    if not 1 <= n <= 3999:
        raise ValueError("Number must be between 1 and 3999")
    result = []
    for value, numeral in ROMAN_MAP:
        while n >= value:
            result.append(numeral)
            n -= value
    return "".join(result)


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string to an integer."""
    total, prev = 0, 0
    for ch in reversed(s.upper()):
        val = ROMAN_VALUES[ch]
        total += val if val >= prev else -val
        prev = val
    return total


if __name__ == "__main__":
    for num in [1, 4, 9, 42, 99, 399, 1994, 2024]:
        roman = int_to_roman(num)
        back = roman_to_int(roman)
        print(f"{num:>5} -> {roman:<15} -> {back}")
