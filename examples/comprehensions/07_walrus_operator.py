"""Comprehensions with the walrus operator (:=), Python 3.8+."""

import math


def filter_with_computation(nums):
    """Compute once, filter and keep the computed value."""
    return [(x, y) for x in nums if (y := x ** 2 + 1) > 10]


def find_expensive_matches(data):
    """Avoid calling an expensive function twice."""
    return [result for item in data if (result := len(item.split())) > 2]


def running_total(nums):
    """Build a running total list using walrus in comprehension."""
    total = 0
    return [(total := total + x) for x in nums]


def filter_with_sqrt(nums):
    """Filter numbers whose sqrt is an integer."""
    return [
        (n, int(root))
        for n in nums
        if (root := math.isqrt(n)) * root == n
    ]


if __name__ == "__main__":
    print(f"Filter computed: {filter_with_computation(range(1, 6))}")
    data = ["hi", "hello world foo", "a b c d", "ok"]
    print(f"Word count > 2: {find_expensive_matches(data)}")
    print(f"Running total: {running_total([1, 2, 3, 4, 5])}")
    print(f"Perfect squares: {filter_with_sqrt(range(1, 26))}")
