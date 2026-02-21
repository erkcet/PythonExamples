"""Generators as context managers using contextlib."""

from contextlib import contextmanager
import time


@contextmanager
def timer(label):
    """Context manager that times the enclosed block."""
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"{label}: {elapsed:.4f}s")


@contextmanager
def temporary_value(obj, attr, value):
    """Temporarily set an attribute, restoring it on exit."""
    original = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield value
    finally:
        setattr(obj, attr, original)


@contextmanager
def managed_list():
    """Provide a list that reports its contents on exit."""
    items = []
    try:
        yield items
    finally:
        print(f"List had {len(items)} items: {items}")


if __name__ == "__main__":
    with timer("Sum"):
        total = sum(range(1_000_000))
    print(f"Total: {total}")

    with managed_list() as lst:
        lst.extend([1, 2, 3])
        lst.append(4)
