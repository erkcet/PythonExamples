"""Set comprehensions for concise set construction."""


def unique_lengths(words):
    """Get the set of unique word lengths."""
    return {len(w) for w in words}


def vowels_in_text(text):
    """Extract unique vowels present in text."""
    return {ch for ch in text.lower() if ch in "aeiou"}


def pythagorean_triples(limit):
    """Find Pythagorean triples up to limit using set comprehension."""
    return {
        (a, b, c)
        for a in range(1, limit)
        for b in range(a, limit)
        for c in range(b, limit)
        if a * a + b * b == c * c
    }


def flatten_unique(nested):
    """Flatten a nested list and keep only unique elements."""
    return {item for sublist in nested for item in sublist}


if __name__ == "__main__":
    words = ["hello", "world", "hi", "python", "code"]
    print(f"Unique lengths: {unique_lengths(words)}")
    print(f"Vowels in 'Hello World': {vowels_in_text('Hello World')}")
    print(f"Triples up to 20: {pythagorean_triples(20)}")
    nested = [[1, 2, 3], [3, 4, 5], [5, 6, 1]]
    print(f"Flattened unique: {flatten_unique(nested)}")
