"""Count the frequency of each character in a string and display a histogram."""

from collections import Counter


def char_frequency(s):
    """Return character frequencies, ignoring spaces."""
    return Counter(ch.lower() for ch in s if not ch.isspace())


if __name__ == "__main__":
    text = "Mississippi"
    freq = char_frequency(text)
    print(f"Character frequencies in '{text}':")
    for ch, count in sorted(freq.items(), key=lambda x: -x[1]):
        bar = "#" * count
        print(f"  '{ch}': {count} {bar}")
