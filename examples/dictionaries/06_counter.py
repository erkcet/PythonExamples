"""Counter for frequency counting and common operations."""

from collections import Counter


def basic_counting(items):
    """Count occurrences of each item."""
    return Counter(items)


def most_common_words(text, n=3):
    """Find the n most common words in text."""
    words = text.lower().split()
    return Counter(words).most_common(n)


def counter_arithmetic():
    """Demonstrate addition and subtraction of Counters."""
    a = Counter({"apples": 3, "oranges": 2})
    b = Counter({"apples": 1, "bananas": 4})
    return a + b, a - b, a & b, a | b


def character_frequency(text):
    """Get character frequency sorted by count."""
    counts = Counter(text.lower())
    return counts.most_common()


if __name__ == "__main__":
    data = ["red", "blue", "red", "green", "blue", "red"]
    print(f"Counts: {basic_counting(data)}")
    text = "the cat sat on the mat the cat"
    print(f"Top words: {most_common_words(text)}")
    add, sub, inter, union = counter_arithmetic()
    print(f"Add: {add}, Sub: {sub}")
    print(f"Inter: {inter}, Union: {union}")
    print(f"Char freq: {character_frequency('Hello World')[:5]}")
