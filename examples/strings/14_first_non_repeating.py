"""Find the first non-repeating character in a string."""

from collections import OrderedDict


def first_non_repeating(s):
    """Return the first character that appears exactly once."""
    counts = OrderedDict()
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch, count in counts.items():
        if count == 1:
            return ch
    return None


if __name__ == "__main__":
    tests = ["aabbcdc", "aabb", "abcdef", "stress"]
    for t in tests:
        result = first_non_repeating(t)
        if result:
            print(f"'{t}' -> first non-repeating: '{result}'")
        else:
            print(f"'{t}' -> no non-repeating character")
