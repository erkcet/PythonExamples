"""Rabin-Karp string matching algorithm using rolling hash."""


def rabin_karp(text, pattern, base=256, mod=101):
    """Find all occurrences of pattern in text using Rabin-Karp."""
    n, m = len(text), len(pattern)
    if m > n:
        return []
    h_pattern = 0
    h_text = 0
    power = pow(base, m - 1, mod)
    matches = []

    for i in range(m):
        h_pattern = (base * h_pattern + ord(pattern[i])) % mod
        h_text = (base * h_text + ord(text[i])) % mod

    for i in range(n - m + 1):
        if h_pattern == h_text and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            h_text = (base * (h_text - ord(text[i]) * power) + ord(text[i + m])) % mod
            h_text = (h_text + mod) % mod
    return matches


def rolling_hash(s, base=256, mod=101):
    """Compute the rolling hash of a string."""
    h = 0
    for c in s:
        h = (base * h + ord(c)) % mod
    return h


if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    print(f"Text:    '{text}'")
    print(f"Pattern: '{pattern}'")
    print(f"Found at: {rabin_karp(text, pattern)}")
    print(f"\nHash of 'GEEK': {rolling_hash('GEEK')}")
    print(f"Multi-match: {rabin_karp('AABAACAADAABAABA', 'AABA')}")
