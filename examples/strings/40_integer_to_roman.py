"""Convert an integer to a Roman numeral string."""


def int_to_roman(num):
    """Convert an integer (1-3999) to Roman numeral."""
    val_syms = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
    ]
    result = []
    for value, symbol in val_syms:
        while num >= value:
            result.append(symbol)
            num -= value
    return ''.join(result)


if __name__ == "__main__":
    numbers = [3, 4, 9, 42, 1994, 2024, 890, 3999]
    for n in numbers:
        print(f"{n:5d} = {int_to_roman(n)}")
