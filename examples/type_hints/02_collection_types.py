"""Collection type hints: List, Dict, Set, Tuple annotations."""


def average(numbers: list[float]) -> float:
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0.0


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word."""
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def unique_letters(word: str) -> set[str]:
    """Return the set of unique letters in a word."""
    return set(word.lower())


def min_max(values: list[int]) -> tuple[int, int]:
    """Return a tuple of (min, max) from a list."""
    return (min(values), max(values))


def demonstrate_collections():
    """Show functions using collection type hints."""
    print(f"Average: {average([10.0, 20.0, 30.0])}")
    print(f"Words:   {word_count('the cat sat on the mat')}")
    print(f"Unique:  {sorted(unique_letters('banana'))}")
    print(f"MinMax:  {min_max([5, 2, 9, 1, 7])}")


if __name__ == "__main__":
    demonstrate_collections()
