"""Memoization decorator for caching function results."""

import functools


def memoize(func):
    """Simple memoization decorator using a dictionary cache."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache
    wrapper.cache_clear = cache.clear
    return wrapper


@memoize
def fibonacci(n):
    """Compute nth Fibonacci number with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@functools.lru_cache(maxsize=128)
def factorial(n):
    """Compute factorial with stdlib lru_cache."""
    return 1 if n <= 1 else n * factorial(n - 1)


if __name__ == "__main__":
    print("Fibonacci with memoize:")
    for i in [10, 20, 30, 40]:
        print(f"  fib({i}) = {fibonacci(i)}")
    print(f"  Cache size: {len(fibonacci.cache)}")
    print("\nFactorial with lru_cache:")
    for i in [5, 10, 15]:
        print(f"  {i}! = {factorial(i)}")
    print(f"  Cache info: {factorial.cache_info()}")
