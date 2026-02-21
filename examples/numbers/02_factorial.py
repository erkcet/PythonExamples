"""Calculate factorial iteratively and recursively."""


def factorial_iterative(n: int) -> int:
    """Calculate n! using iteration."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Calculate n! using recursion."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    for i in range(11):
        it = factorial_iterative(i)
        rec = factorial_recursive(i)
        assert it == rec
        print(f"{i:>2}! = {it}")
