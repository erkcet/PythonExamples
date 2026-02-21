"""Calculate the Levenshtein (edit) distance between two strings."""


def levenshtein(s1, s2):
    """Return the minimum number of edits to transform s1 into s2."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)
    return dp[m][n]


if __name__ == "__main__":
    pairs = [("kitten", "sitting"), ("flaw", "lawn"), ("", "abc"), ("python", "python")]
    for a, b in pairs:
        print(f"distance('{a}', '{b}') = {levenshtein(a, b)}")
