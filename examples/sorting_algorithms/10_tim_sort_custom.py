"""Custom Sorting with Python's Built-in TimSort.

Demonstrates using sorted() and list.sort() with custom key functions
and comparison logic. Python uses TimSort: O(n log n), stable.
"""


def sort_by_length(words: list) -> list:
    """Sort strings by their length."""
    return sorted(words, key=len)


def sort_by_last_char(words: list) -> list:
    """Sort strings by their last character."""
    return sorted(words, key=lambda w: w[-1])


def sort_dicts_by_key(items: list, key: str, reverse: bool = False) -> list:
    """Sort a list of dictionaries by a given key."""
    return sorted(items, key=lambda d: d[key], reverse=reverse)


def multi_key_sort(data: list) -> list:
    """Sort tuples by second element, then first element."""
    return sorted(data, key=lambda x: (x[1], x[0]))


if __name__ == "__main__":
    words = ["banana", "pie", "apple", "fig", "kiwi"]
    print(f"By length:    {sort_by_length(words)}")
    print(f"By last char: {sort_by_last_char(words)}")

    people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    print(f"By age: {sort_dicts_by_key(people, 'age')}")

    pairs = [(2, 'b'), (1, 'a'), (3, 'a'), (1, 'b')]
    print(f"Multi-key: {multi_key_sort(pairs)}")
