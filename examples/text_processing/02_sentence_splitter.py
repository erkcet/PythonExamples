"""Split text into individual sentences handling common abbreviations."""

import re


def split_sentences(text):
    """Split text into sentences at period, question mark, or exclamation mark."""
    pattern = r'(?<=[.!?])\s+'
    sentences = re.split(pattern, text.strip())
    return [s.strip() for s in sentences if s.strip()]


if __name__ == "__main__":
    text = ("Dr. Smith went to Washington. He arrived at 3 p.m. "
            "Was it sunny? Yes! The weather was great. "
            "He stayed for two days.")
    sentences = split_sentences(text)
    print(f"Found {len(sentences)} sentences:")
    for i, s in enumerate(sentences, 1):
        print(f"  {i}. {s}")
