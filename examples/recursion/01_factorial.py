"""Factorial Using Recursion.

Computes n! = n * (n-1) * ... * 1 recursively.
Includes both recursive and tail-call style implementations.
"""


def factorial(n: int) -> int:
    """Compute factorial of n recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def factorial_tail(n: int, accumulator: int = 1) -> int:
    """Compute factorial using tail recursion style."""
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)


if __name__ == "__main__":
    for i in range(11):
        print(f"{i}! = {factorial(i)}")
    print(f"\nTail-recursive 20! = {factorial_tail(20)}")
