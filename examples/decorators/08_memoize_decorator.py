"""Memoization decorator: cache function results by arguments."""

from functools import wraps


def memoize(func):
    """Cache results of function calls keyed by arguments."""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache
    wrapper.clear_cache = cache.clear
    return wrapper


@memoize
def fibonacci(n):
    """Compute Fibonacci number with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@memoize
def expensive_compute(x, y):
    """Simulate an expensive computation."""
    print(f"  Computing {x} + {y}...")
    return x + y


if __name__ == "__main__":
    print(f"fib(30) = {fibonacci(30)}")
    print(f"Cache size: {len(fibonacci.cache)}")

    print(expensive_compute(3, 4))
    print(expensive_compute(3, 4))  # cached, no print
    print(f"Cache: {expensive_compute.cache}")
