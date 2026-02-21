"""Check if a string follows a given word pattern (e.g., 'abba' matches 'dog cat cat dog')."""


def word_pattern(pattern, s):
    """Return True if the string follows the given pattern."""
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for ch, word in zip(pattern, words):
        if ch in char_to_word and char_to_word[ch] != word:
            return False
        if word in word_to_char and word_to_char[word] != ch:
            return False
        char_to_word[ch] = word
        word_to_char[word] = ch
    return True


if __name__ == "__main__":
    tests = [
        ("abba", "dog cat cat dog"),
        ("abba", "dog cat cat fish"),
        ("aaaa", "dog cat cat dog"),
        ("abab", "red blue red blue"),
    ]
    for pattern, s in tests:
        print(f"pattern='{pattern}', s='{s}' -> {word_pattern(pattern, s)}")
