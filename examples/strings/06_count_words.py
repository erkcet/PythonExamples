"""Count the number of words in a string using different approaches."""


def count_words_split(s):
    """Count words by splitting on whitespace."""
    return len(s.split())


def count_words_manual(s):
    """Count words by tracking transitions from space to non-space."""
    count = 0
    in_word = False
    for ch in s:
        if ch.isspace():
            in_word = False
        elif not in_word:
            in_word = True
            count += 1
    return count


if __name__ == "__main__":
    texts = ["Hello World", "  multiple   spaces  here  ", "single", ""]
    for text in texts:
        print(f"'{text}' -> split: {count_words_split(text)}, manual: {count_words_manual(text)}")
