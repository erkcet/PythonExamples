"""Calculate the Flesch Reading Ease score for a given text."""

import re


def count_syllables(word):
    """Estimate syllable count for a word."""
    word = word.lower()
    if word.endswith('e') and len(word) > 2:
        word = word[:-1]
    return max(1, len(re.findall(r'[aeiouy]+', word)))


def flesch_reading_ease(text):
    """Calculate Flesch Reading Ease score."""
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    words = re.findall(r'[a-zA-Z]+', text)
    n_sent, n_words = len(sentences), len(words)
    if n_sent == 0 or n_words == 0:
        return 0.0
    n_syl = sum(count_syllables(w) for w in words)
    return round(206.835 - 1.015 * (n_words / n_sent) - 84.6 * (n_syl / n_words), 1)


if __name__ == "__main__":
    texts = {
        "Simple": "The cat sat on the mat. It was a good cat.",
        "Medium": "Python provides powerful capabilities for data analysis.",
        "Hard": "Notwithstanding presuppositions, epistemological ramifications necessitate deliberation.",
    }
    for label, text in texts.items():
        score = flesch_reading_ease(text)
        print(f"{label:8s} (score {score:5.1f}): {text[:55]}...")
