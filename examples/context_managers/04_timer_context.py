"""Timer context manager for measuring code execution time."""

import time
from contextlib import contextmanager


class Timer:
    """A reusable timer context manager."""

    def __init__(self, label="Timer"):
        self.label = label
        self.elapsed = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *exc):
        self.elapsed = time.perf_counter() - self.start
        print(f"[{self.label}] {self.elapsed:.4f}s")
        return False


@contextmanager
def quick_timer(label="timer"):
    """A simple generator-based timer."""
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"[{label}] {elapsed:.4f}s")


def slow_computation(n):
    """Simulate work."""
    total = sum(i * i for i in range(n))
    return total


if __name__ == "__main__":
    with Timer("class-based") as t:
        slow_computation(100_000)
    print(f"Elapsed available after: {t.elapsed:.4f}s")

    with quick_timer("generator-based"):
        slow_computation(100_000)

    with Timer("comparison"):
        time.sleep(0.05)
