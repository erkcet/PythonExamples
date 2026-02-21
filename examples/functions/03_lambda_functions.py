"""Lambda functions and common use cases."""


# Simple lambda
square = lambda x: x ** 2

# Lambda as sort key
pairs = [(1, "b"), (3, "a"), (2, "c")]


def sort_by_second(items):
    """Sort a list of tuples by the second element using a lambda."""
    return sorted(items, key=lambda item: item[1])


def apply_operation(x, y, op=lambda a, b: a + b):
    """Apply a binary operation (default: addition) to two values."""
    return op(x, y)


def make_multiplier(n):
    """Return a lambda that multiplies its argument by n."""
    return lambda x: x * n


if __name__ == "__main__":
    print(f"square(5) = {square(5)}")
    print(f"Sorted by second: {sort_by_second(pairs)}")
    print(f"Default op: {apply_operation(3, 4)}")
    print(f"Multiply op: {apply_operation(3, 4, op=lambda a, b: a * b)}")
    double = make_multiplier(2)
    print(f"double(7) = {double(7)}")
