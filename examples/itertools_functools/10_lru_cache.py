"""functools.lru_cache for memoizing function results."""

from functools import lru_cache
import time


@lru_cache(maxsize=128)
def fibonacci(n):
    """Compute Fibonacci number with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache(maxsize=64)
def factorial(n):
    """Compute factorial with memoization."""
    return 1 if n <= 1 else n * factorial(n - 1)


@lru_cache(maxsize=None)
def expensive_computation(x, y):
    """Simulate an expensive computation (cached with no size limit)."""
    time.sleep(0.01)  # simulate work
    return x ** y + y ** x


if __name__ == "__main__":
    # Fibonacci
    print(f"fib(10): {fibonacci(10)}")
    print(f"fib(50): {fibonacci(50)}")
    print(f"Cache info: {fibonacci.cache_info()}")

    # Factorial
    print(f"\n5! = {factorial(5)}")
    print(f"10! = {factorial(10)}")

    # Timing cached vs uncached
    start = time.time()
    expensive_computation(100, 200)
    first = time.time() - start

    start = time.time()
    expensive_computation(100, 200)
    second = time.time() - start
    print(f"\nFirst call:  {first:.4f}s")
    print(f"Cached call: {second:.6f}s")

    # Clear cache
    fibonacci.cache_clear()
    print(f"\nAfter clear: {fibonacci.cache_info()}")
