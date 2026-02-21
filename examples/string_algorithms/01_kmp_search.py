"""KMP (Knuth-Morris-Pratt) string matching algorithm."""


def build_kmp_table(pattern):
    """Build the partial match (failure function) table."""
    table = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            table[i] = length
            i += 1
        elif length:
            length = table[length - 1]
        else:
            table[i] = 0
            i += 1
    return table


def kmp_search(text, pattern):
    """Find all occurrences of pattern in text using KMP. Returns indices."""
    if not pattern:
        return []
    table = build_kmp_table(pattern)
    matches = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = table[j - 1]
    return matches


if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    print(f"KMP table: {build_kmp_table(pattern)}")
    print(f"Found at indices: {kmp_search(text, pattern)}")
    print(f"Search 'ABCD' in 'ABCABCDABCABCD': {kmp_search('ABCABCDABCABCD', 'ABCD')}")
