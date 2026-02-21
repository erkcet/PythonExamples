"""Check if two strings are anagrams of each other."""

from collections import Counter


def are_anagrams(s1, s2):
    """Return True if s1 and s2 are anagrams (ignoring case and spaces)."""
    clean1 = s1.replace(" ", "").lower()
    clean2 = s2.replace(" ", "").lower()
    return Counter(clean1) == Counter(clean2)


if __name__ == "__main__":
    pairs = [
        ("listen", "silent"),
        ("hello", "world"),
        ("Astronomer", "Moon starer"),
        ("rail safety", "fairy tales"),
    ]
    for a, b in pairs:
        print(f"'{a}' & '{b}' -> anagram: {are_anagrams(a, b)}")
