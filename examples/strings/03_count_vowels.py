"""Count the number of vowels in a string."""


def count_vowels(s):
    """Return a dict with counts for each vowel found."""
    vowels = "aeiouAEIOU"
    counts = {}
    for ch in s:
        if ch in vowels:
            key = ch.lower()
            counts[key] = counts.get(key, 0) + 1
    return counts


if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog"
    result = count_vowels(text)
    total = sum(result.values())
    print(f"Text: {text}")
    print(f"Vowel counts: {result}")
    print(f"Total vowels: {total}")
