"""Counter for frequency analysis of elements."""

from collections import Counter


def word_frequency(text):
    """Count word frequencies in a text string."""
    words = text.lower().split()
    return Counter(words)


def char_frequency(text):
    """Count character frequencies, excluding spaces."""
    return Counter(c for c in text.lower() if c != " ")


def top_n_items(data, n=3):
    """Find the n most common items."""
    return Counter(data).most_common(n)


if __name__ == "__main__":
    text = "the cat sat on the mat the cat ate the rat"
    freq = word_frequency(text)
    print("Word frequencies:", freq)
    print("Most common 3:", freq.most_common(3))

    chars = char_frequency("hello world")
    print(f"\nChar frequencies: {chars}")

    grades = ["A", "B", "A", "C", "B", "A", "D", "B", "A"]
    print(f"\nTop grades: {top_n_items(grades, 2)}")
    print(f"Total count: {sum(Counter(grades).values())}")

    # Elements iterator
    c = Counter(a=2, b=3)
    print(f"Elements: {sorted(c.elements())}")
