"""Execution timer as decorator and context manager."""

import time
import functools


def timer(func):
    """Decorator that measures and prints execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper


class Timer:
    """Context manager for timing code blocks."""

    def __init__(self, label="Block"):
        self.label = label
        self.elapsed = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
        print(f"  {self.label} took {self.elapsed:.6f}s")


@timer
def slow_sum(n):
    """Sum numbers from 0 to n."""
    return sum(range(n))


if __name__ == "__main__":
    print("Decorator timer:")
    slow_sum(1_000_000)
    print("\nContext manager timer:")
    with Timer("List comprehension") as t:
        data = [x ** 2 for x in range(100_000)]
    print(f"  (elapsed attribute: {t.elapsed:.6f}s)")
