"""Find unique characters in strings using sets."""


def unique_chars(text):
    """Return sorted unique characters in text."""
    return sorted(set(text))


def first_unique_char(text):
    """Find the first character that appears only once."""
    from collections import Counter
    counts = Counter(text)
    for ch in text:
        if counts[ch] == 1:
            return ch
    return None


def common_chars(s1, s2):
    """Find characters common to both strings."""
    return sorted(set(s1) & set(s2))


def chars_in_all_words(words):
    """Find characters present in every word."""
    if not words:
        return set()
    result = set(words[0])
    for word in words[1:]:
        result &= set(word)
    return sorted(result)


if __name__ == "__main__":
    text = "abracadabra"
    print(f"Unique chars: {unique_chars(text)}")
    print(f"First unique: {first_unique_char(text)}")
    print(f"Common ('hello','world'): {common_chars('hello', 'world')}")
    words = ["apple", "pear", "grape"]
    print(f"In all words: {chars_in_all_words(words)}")
