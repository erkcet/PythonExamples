"""Check if a number is even or odd."""


def is_even(n: int) -> bool:
    """Return True if n is even, False if odd."""
    return n % 2 == 0


def classify(n: int) -> str:
    """Return 'even' or 'odd' for the given integer."""
    return "even" if is_even(n) else "odd"


def classify_list(numbers: list[int]) -> dict[str, list[int]]:
    """Separate a list of numbers into even and odd groups."""
    result = {"even": [], "odd": []}
    for n in numbers:
        result[classify(n)].append(n)
    return result


if __name__ == "__main__":
    for num in range(-3, 6):
        print(f"{num:>3} is {classify(num)}")
    print()
    groups = classify_list(range(1, 11))
    print(f"Even: {groups['even']}")
    print(f"Odd:  {groups['odd']}")
