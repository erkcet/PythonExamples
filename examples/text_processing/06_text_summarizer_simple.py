"""Summarize text by extracting the most important sentences based on word frequency."""

import re
from collections import Counter


def summarize(text, num_sentences=2):
    """Extract top sentences by cumulative word importance."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    words = re.findall(r'[a-z]+', text.lower())
    freq = Counter(words)
    scored = []
    for sent in sentences:
        sent_words = re.findall(r'[a-z]+', sent.lower())
        score = sum(freq[w] for w in sent_words)
        scored.append((score, sent))
    scored.sort(reverse=True)
    top = [s for _, s in scored[:num_sentences]]
    return ' '.join(top)


if __name__ == "__main__":
    text = ("Python is a popular programming language. "
            "It is used for web development and data science. "
            "Python has simple syntax that is easy to learn. "
            "Many developers choose Python for its readability. "
            "Python supports multiple programming paradigms.")
    print("Original text:")
    print(f"  {text}")
    print(f"\nSummary ({2} sentences):")
    print(f"  {summarize(text, 2)}")
