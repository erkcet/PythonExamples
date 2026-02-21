"""lru_cache and caching patterns for expensive computations."""

from functools import lru_cache


@lru_cache(maxsize=128)
def fibonacci(n):
    """Compute the nth Fibonacci number with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache(maxsize=None)
def factorial(n):
    """Compute n! with unbounded cache."""
    return 1 if n <= 1 else n * factorial(n - 1)


def manual_cache_example():
    """Demonstrate a simple manual dictionary cache."""
    cache = {}

    def expensive(x):
        if x not in cache:
            cache[x] = x ** x
        return cache[x]

    return expensive


if __name__ == "__main__":
    print(f"fib(30) = {fibonacci(30)}")
    print(f"Cache info: {fibonacci.cache_info()}")
    print(f"10! = {factorial(10)}")
    compute = manual_cache_example()
    print(f"5^5 = {compute(5)}")
