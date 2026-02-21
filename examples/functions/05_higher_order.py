"""Higher-order functions: map, filter, reduce."""

from functools import reduce


def apply_map(numbers):
    """Double each number using map."""
    return list(map(lambda x: x * 2, numbers))


def apply_filter(numbers):
    """Keep only even numbers using filter."""
    return list(filter(lambda x: x % 2 == 0, numbers))


def apply_reduce(numbers):
    """Compute the product of all numbers using reduce."""
    return reduce(lambda a, b: a * b, numbers, 1)


def transform_pipeline(data):
    """Chain map and filter: square numbers, then keep those > 10."""
    squared = map(lambda x: x ** 2, data)
    return list(filter(lambda x: x > 10, squared))


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print(f"Doubled: {apply_map(nums)}")
    print(f"Evens: {apply_filter(nums)}")
    print(f"Product: {apply_reduce(nums)}")
    print(f"Squared > 10: {transform_pipeline(nums)}")
