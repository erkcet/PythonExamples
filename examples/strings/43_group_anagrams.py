"""Group a list of strings into anagram groups."""

from collections import defaultdict


def group_anagrams(words):
    """Group words that are anagrams of each other."""
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.lower()))
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "opt", "top", "pot"]
    groups = group_anagrams(words)
    print(f"Words: {words}")
    print(f"\nAnagram groups ({len(groups)} groups):")
    for i, group in enumerate(groups, 1):
        print(f"  Group {i}: {group}")
