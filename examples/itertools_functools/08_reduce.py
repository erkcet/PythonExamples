"""functools.reduce for cumulative computation over sequences."""

from functools import reduce
import operator


def product(numbers):
    """Calculate the product of all numbers using reduce."""
    return reduce(operator.mul, numbers, 1)


def flatten(nested_lists):
    """Flatten a list of lists using reduce."""
    return reduce(lambda acc, lst: acc + lst, nested_lists, [])


def compose(*functions):
    """Compose multiple functions right-to-left using reduce."""
    return reduce(lambda f, g: lambda x: f(g(x)), functions)


def deep_get(dictionary, keys):
    """Safely navigate nested dict keys using reduce."""
    return reduce(lambda d, key: d.get(key, {}) if isinstance(d, dict) else None, keys, dictionary)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(f"Product of {nums}: {product(nums)}")

    nested = [[1, 2], [3, 4], [5]]
    print(f"Flatten {nested}: {flatten(nested)}")

    # Function composition
    double = lambda x: x * 2
    add_one = lambda x: x + 1
    square = lambda x: x ** 2
    transform = compose(square, add_one, double)  # square(add_one(double(x)))
    print(f"\nsquare(add_one(double(3))): {transform(3)}")

    data = {"a": {"b": {"c": 42}}}
    print(f"Deep get ['a','b','c']: {deep_get(data, ['a', 'b', 'c'])}")
    print(f"Deep get ['a','x']:     {deep_get(data, ['a', 'x'])}")
