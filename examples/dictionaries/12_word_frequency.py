"""Word frequency counter with various analyses."""

from collections import Counter
import re


def word_frequencies(text):
    """Count word frequencies, ignoring case and punctuation."""
    words = re.findall(r"[a-z]+", text.lower())
    return Counter(words)


def top_n_words(text, n=5):
    """Get the top n most frequent words."""
    return word_frequencies(text).most_common(n)


def hapax_legomena(text):
    """Find words that appear exactly once."""
    freq = word_frequencies(text)
    return [word for word, count in freq.items() if count == 1]


def frequency_distribution(text):
    """Map frequency -> list of words with that frequency."""
    freq = word_frequencies(text)
    dist = {}
    for word, count in freq.items():
        dist.setdefault(count, []).append(word)
    return dict(sorted(dist.items(), reverse=True))


if __name__ == "__main__":
    text = "the cat sat on the mat and the cat sat on the hat"
    print(f"Frequencies: {word_frequencies(text)}")
    print(f"Top 3: {top_n_words(text, 3)}")
    print(f"Hapax: {hapax_legomena(text)}")
    print(f"Distribution: {frequency_distribution(text)}")
