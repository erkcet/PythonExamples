"""Generator expressions: concise lazy iteration."""


def sum_of_squares(n):
    """Sum squares of 1..n using a generator expression."""
    return sum(x ** 2 for x in range(1, n + 1))


def first_match(iterable, predicate):
    """Return the first item matching predicate, or None."""
    return next((x for x in iterable if predicate(x)), None)


if __name__ == "__main__":
    # Generator expression vs list comprehension
    squares_gen = (x ** 2 for x in range(5))
    squares_list = [x ** 2 for x in range(5)]
    print(f"Generator: {squares_gen}")
    print(f"List: {squares_list}")
    print(f"From gen: {list(squares_gen)}")

    print(f"Sum of squares(10): {sum_of_squares(10)}")

    nums = range(100)
    print(f"First > 50 and even: {first_match(nums, lambda x: x > 50 and x % 2 == 0)}")

    # Memory-efficient: process large range without storing all values
    total = sum(x for x in range(1_000_000) if x % 3 == 0)
    print(f"Sum of multiples of 3 under 1M: {total}")
