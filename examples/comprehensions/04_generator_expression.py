"""Generator expressions for memory-efficient iteration."""

import sys


def sum_of_squares(n):
    """Sum squares lazily with a generator expression."""
    return sum(x ** 2 for x in range(1, n + 1))


def first_match(iterable, predicate):
    """Find the first element matching a predicate."""
    return next((x for x in iterable if predicate(x)), None)


def memory_comparison(n):
    """Compare memory usage of list vs generator."""
    lst = [x ** 2 for x in range(n)]
    gen = (x ** 2 for x in range(n))
    return sys.getsizeof(lst), sys.getsizeof(gen)


def chained_generators(data):
    """Chain generator operations like a pipeline."""
    stripped = (line.strip() for line in data)
    non_empty = (line for line in stripped if line)
    uppered = (line.upper() for line in non_empty)
    return list(uppered)


if __name__ == "__main__":
    print(f"Sum of squares(100): {sum_of_squares(100)}")
    print(f"First even > 10: {first_match(range(1, 100), lambda x: x % 2 == 0 and x > 10)}")
    list_mem, gen_mem = memory_comparison(10000)
    print(f"Memory - list: {list_mem} bytes, gen: {gen_mem} bytes")
    lines = ["  hello  ", "", "  world  ", "   ", "  python  "]
    print(f"Pipeline: {chained_generators(lines)}")
