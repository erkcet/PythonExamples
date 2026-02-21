"""Translate English text to Pig Latin."""

import re

VOWELS = set("aeiouAEIOU")


def to_pig_latin(word):
    """Convert a single word to Pig Latin."""
    if word[0] in VOWELS:
        return word + "yay"
    for i, ch in enumerate(word):
        if ch in VOWELS:
            pig = word[i:] + word[:i] + "ay"
            if word[0].isupper():
                pig = pig.capitalize()
            return pig
    return word + "ay"


def translate(text):
    """Translate a full sentence to Pig Latin."""
    tokens = re.findall(r"[a-zA-Z]+|[^a-zA-Z]+", text)
    return ''.join(to_pig_latin(t) if t[0].isalpha() else t for t in tokens)


if __name__ == "__main__":
    sentences = ["Hello world", "Python is awesome", "The quick brown fox"]
    for s in sentences:
        print(f"{s:25s} -> {translate(s)}")
