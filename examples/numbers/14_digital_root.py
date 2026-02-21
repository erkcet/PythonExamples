"""Calculate digital root of a number."""


def digital_root_iterative(n: int) -> int:
    """Calculate digital root by repeatedly summing digits."""
    n = abs(n)
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


def digital_root_formula(n: int) -> int:
    """Calculate digital root using the direct formula."""
    n = abs(n)
    if n == 0:
        return 0
    return 1 + (n - 1) % 9


def additive_persistence(n: int) -> int:
    """Count how many times digits must be summed to reach a single digit."""
    n, count = abs(n), 0
    while n >= 10:
        n = sum(int(d) for d in str(n))
        count += 1
    return count


if __name__ == "__main__":
    test_numbers = [0, 5, 39, 199, 9999, 12345]
    for num in test_numbers:
        dr = digital_root_iterative(num)
        assert dr == digital_root_formula(num)
        ap = additive_persistence(num)
        print(f"{num:>6}: digital root = {dr}, persistence = {ap}")
