"""Callable type hints for functions that accept other functions."""

from typing import Callable


def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:
    """Apply a binary operation to two integers."""
    return op(x, y)


def make_multiplier(factor: int) -> Callable[[int], int]:
    """Return a function that multiplies by a fixed factor."""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier


def transform_list(items: list[str], func: Callable[[str], str]) -> list[str]:
    """Apply a transformation function to each item."""
    return [func(item) for item in items]


def demonstrate_callables():
    """Show Callable type hints with higher-order functions."""
    print(apply_operation(10, 3, lambda a, b: a + b))
    print(apply_operation(10, 3, lambda a, b: a * b))

    triple = make_multiplier(3)
    print(f"triple(7) = {triple(7)}")

    words = ["hello", "world"]
    print(transform_list(words, str.upper))
    print(transform_list(words, lambda s: s[::-1]))


if __name__ == "__main__":
    demonstrate_callables()
