"""Dictionary comprehensions."""


def squares_dict(n):
    """Map numbers to their squares."""
    return {x: x ** 2 for x in range(1, n + 1)}


def invert_dict(d):
    """Swap keys and values."""
    return {v: k for k, v in d.items()}


def filter_dict(d, threshold):
    """Keep only entries above a threshold value."""
    return {k: v for k, v in d.items() if v > threshold}


def word_lengths(words):
    """Map each word to its length."""
    return {w: len(w) for w in words}


def merge_with_comprehension(d1, d2):
    """Merge two dicts, d2 values take precedence."""
    return {k: v for d in (d1, d2) for k, v in d.items()}


if __name__ == "__main__":
    print(f"Squares: {squares_dict(5)}")
    original = {"a": 1, "b": 2, "c": 3}
    print(f"Inverted: {invert_dict(original)}")
    scores = {"Alice": 85, "Bob": 62, "Charlie": 91, "Diana": 58}
    print(f"Above 70: {filter_dict(scores, 70)}")
    print(f"Word lengths: {word_lengths(['hello', 'world', 'python'])}")
    print(f"Merged: {merge_with_comprehension({'a': 1}, {'a': 2, 'b': 3})}")
