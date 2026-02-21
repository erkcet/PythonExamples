"""Longest common substring using dynamic programming."""


def longest_common_substring(s1, s2):
    """Find the longest common substring between two strings."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len, end_idx = 0, 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_idx = i
    return s1[end_idx - max_len:end_idx]


def all_common_substrings(s1, s2, min_length=2):
    """Find all common substrings of at least min_length."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    results = set()
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] >= min_length:
                    results.add(s1[i - dp[i][j]:i])
    return sorted(results, key=len, reverse=True)


if __name__ == "__main__":
    pairs = [("ABABC", "BABCBA"), ("GeeksforGeeks", "GeeksQuiz"), ("abcde", "fghij")]
    for s1, s2 in pairs:
        lcs = longest_common_substring(s1, s2)
        print(f"'{s1}' & '{s2}' -> '{lcs}' (len={len(lcs)})")
    print(f"\nAll common (min 2): {all_common_substrings('ABABC', 'BABCBA')}")
