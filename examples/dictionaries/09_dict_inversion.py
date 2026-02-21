"""Invert key-value pairs in dictionaries."""


def simple_invert(d):
    """Invert a dict (assumes unique values)."""
    return {v: k for k, v in d.items()}


def invert_with_duplicates(d):
    """Invert grouping keys by shared values."""
    inverted = {}
    for k, v in d.items():
        inverted.setdefault(v, []).append(k)
    return inverted


def safe_invert(d):
    """Invert, raising an error on duplicate values."""
    inverted = {}
    for k, v in d.items():
        if v in inverted:
            raise ValueError(f"Duplicate value: {v} (keys: {inverted[v]}, {k})")
        inverted[v] = k
    return inverted


if __name__ == "__main__":
    codes = {"US": 1, "UK": 44, "IN": 91}
    print(f"Simple invert: {simple_invert(codes)}")
    grades = {"Alice": "A", "Bob": "B", "Charlie": "A", "Diana": "B"}
    print(f"With duplicates: {invert_with_duplicates(grades)}")
    try:
        safe_invert(grades)
    except ValueError as e:
        print(f"Safe invert error: {e}")
