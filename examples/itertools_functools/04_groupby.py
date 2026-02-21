"""itertools.groupby for grouping consecutive elements."""

import itertools


def group_consecutive(data, key=None):
    """Group consecutive elements sharing the same key."""
    return [(k, list(g)) for k, g in itertools.groupby(data, key=key)]


def group_by_first_char(words):
    """Group sorted words by their first character."""
    sorted_words = sorted(words, key=lambda w: w[0].lower())
    return {k: list(g) for k, g in itertools.groupby(sorted_words, key=lambda w: w[0].lower())}


def run_length_encode(data):
    """Run-length encode a sequence."""
    return [(char, sum(1 for _ in group)) for char, group in itertools.groupby(data)]


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3, 1, 1]
    print("Consecutive groups:", group_consecutive(nums))

    words = ["apple", "banana", "avocado", "cherry", "blueberry", "apricot"]
    print("\nGrouped by first char:")
    for char, group in group_by_first_char(words).items():
        print(f"  {char}: {group}")

    text = "aaabbbccaab"
    encoded = run_length_encode(text)
    print(f"\nRun-length encode '{text}': {encoded}")

    # Group by even/odd (must sort first!)
    nums = sorted(range(10), key=lambda x: x % 2)
    grouped = group_consecutive(nums, key=lambda x: "even" if x % 2 == 0 else "odd")
    print("Even/odd:", grouped)
