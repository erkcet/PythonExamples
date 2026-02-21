"""Dictionary comprehension patterns."""


def char_positions(text):
    """Map each character to its list of positions."""
    return {ch: [i for i, c in enumerate(text) if c == ch] for ch in set(text)}


def conditional_mapping(d, threshold):
    """Map values above threshold to 'high', else 'low'."""
    return {k: ("high" if v > threshold else "low") for k, v in d.items()}


def enumerate_dict(items):
    """Create a dict mapping index to item."""
    return {i: item for i, item in enumerate(items)}


def swap_keys_values(d):
    """Swap keys and values (assumes unique values)."""
    return {v: k for k, v in d.items()}


if __name__ == "__main__":
    print(f"Char positions: {char_positions('hello')}")
    scores = {"Alice": 85, "Bob": 92, "Charlie": 67}
    print(f"Conditional: {conditional_mapping(scores, 80)}")
    print(f"Enumerated: {enumerate_dict(['a', 'b', 'c'])}")
    codes = {"US": 1, "UK": 44, "IN": 91}
    print(f"Swapped: {swap_keys_values(codes)}")
