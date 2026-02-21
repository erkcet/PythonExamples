"""Estimate the number of syllables in English words using simple heuristics."""

import re


def count_syllables(word):
    """Estimate syllable count using vowel-group heuristic."""
    word = word.lower().strip()
    if not word:
        return 0
    # Remove trailing silent 'e'
    if word.endswith('e') and len(word) > 2:
        word = word[:-1]
    # Count vowel groups
    vowel_groups = re.findall(r'[aeiouy]+', word)
    count = len(vowel_groups)
    return max(1, count)


if __name__ == "__main__":
    words = ["hello", "beautiful", "python", "programming", "the",
             "extraordinary", "simple", "create", "a", "syllable"]
    print(f"{'Word':20s} {'Syllables':>10s}")
    print("-" * 32)
    for w in words:
        print(f"{w:20s} {count_syllables(w):>10d}")
