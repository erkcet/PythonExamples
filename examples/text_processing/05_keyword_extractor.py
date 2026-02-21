"""Extract keywords from text by filtering stop words and ranking by frequency."""

from collections import Counter
import re

STOP_WORDS = {
    "the", "a", "an", "is", "it", "in", "on", "at", "to", "and",
    "or", "of", "for", "with", "as", "by", "from", "that", "this",
    "was", "are", "be", "has", "have", "had", "not", "but", "its",
}


def extract_keywords(text, top_n=5):
    """Extract top keywords by frequency, excluding stop words."""
    words = re.findall(r'[a-z]+', text.lower())
    filtered = [w for w in words if w not in STOP_WORDS and len(w) > 2]
    return Counter(filtered).most_common(top_n)


if __name__ == "__main__":
    text = ("Python programming is great for data science and machine learning. "
            "Python provides powerful libraries for data analysis. "
            "Data science with Python is growing rapidly.")
    keywords = extract_keywords(text, top_n=5)
    print("Top keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")
