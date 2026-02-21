"""Decorator to measure and report function execution time."""

import time
from functools import wraps


def timing(func):
    """Decorator that prints the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper


@timing
def slow_sum(n):
    """Sum numbers with a small delay to simulate work."""
    total = 0
    for i in range(n):
        total += i
    return total


@timing
def fast_sum(n):
    """Sum using the formula n*(n-1)/2."""
    return n * (n - 1) // 2


if __name__ == "__main__":
    result1 = slow_sum(1_000_000)
    result2 = fast_sum(1_000_000)
    print(f"Both equal: {result1 == result2}")
