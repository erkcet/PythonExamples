"""Edit Distance (Levenshtein Distance).

Computes the minimum number of single-character edits (insert,
delete, replace) to transform one string into another. O(m*n).
"""


def edit_distance(s1: str, s2: str) -> int:
    """Return the minimum edit distance between s1 and s2."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # delete
                                    dp[i][j - 1],      # insert
                                    dp[i - 1][j - 1])  # replace
    return dp[m][n]


def edit_distance_optimized(s1: str, s2: str) -> int:
    """Space-optimized edit distance using two rows."""
    m, n = len(s1), len(s2)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev = curr
    return prev[n]


if __name__ == "__main__":
    pairs = [("kitten", "sitting"), ("sunday", "saturday"), ("", "abc")]
    for a, b in pairs:
        dist = edit_distance(a, b)
        print(f"'{a}' -> '{b}': distance = {dist}")
