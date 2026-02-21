"""Count the frequency of each word in a text and display the top results."""

from collections import Counter
import re


def word_frequency(text, top_n=10):
    """Return the most common words and their counts."""
    words = re.findall(r'[a-z]+', text.lower())
    return Counter(words).most_common(top_n)


if __name__ == "__main__":
    sample = ("To be or not to be that is the question "
              "Whether tis nobler in the mind to suffer "
              "The slings and arrows of outrageous fortune "
              "Or to take arms against a sea of troubles")
    print("Word frequencies (top 10):")
    for word, count in word_frequency(sample):
        bar = "#" * count
        print(f"  {word:12s} {count:3d} {bar}")
