"""Truncate a string to a maximum length with an ellipsis suffix."""


def truncate(s, max_len, suffix="..."):
    """Truncate string to max_len characters, appending suffix if truncated."""
    if len(s) <= max_len:
        return s
    return s[:max_len - len(suffix)] + suffix


def truncate_words(s, max_words, suffix="..."):
    """Truncate to a maximum number of words."""
    words = s.split()
    if len(words) <= max_words:
        return s
    return ' '.join(words[:max_words]) + suffix


if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog"
    print(f"Original: {text}")
    print(f"Trunc 20: {truncate(text, 20)}")
    print(f"Trunc 10: {truncate(text, 10)}")
    print(f"Words  5: {truncate_words(text, 5)}")
