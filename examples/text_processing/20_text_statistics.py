"""Compute various statistics about a given text."""

import re
from collections import Counter


def text_stats(text):
    """Return a dictionary of statistics about the text."""
    words = text.split()
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    freq = Counter(w.lower() for w in words)
    avg_len = sum(len(w) for w in words) / max(len(words), 1)
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len(sentences),
        "avg_word_length": round(avg_len, 1),
        "most_common": freq.most_common(3),
    }


if __name__ == "__main__":
    text = ("Python is a great language. It is easy to learn. "
            "Many developers love Python for its simplicity.")
    stats = text_stats(text)
    print("Text Statistics:")
    for key, value in stats.items():
        print(f"  {key:20s}: {value}")
