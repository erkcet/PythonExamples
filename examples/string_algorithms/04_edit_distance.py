"""Edit distance (Levenshtein distance) between two strings."""


def edit_distance(s1, s2):
    """Compute minimum edit distance using dynamic programming."""
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
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]


def edit_operations(s1, s2):
    """Return the sequence of edit operations."""
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
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    ops, i, j = [], m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            ops.append(f"keep '{s1[i - 1]}'")
            i, j = i - 1, j - 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            ops.append(f"replace '{s1[i - 1]}' -> '{s2[j - 1]}'")
            i, j = i - 1, j - 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            ops.append(f"insert '{s2[j - 1]}'")
            j -= 1
        else:
            ops.append(f"delete '{s1[i - 1]}'")
            i -= 1
    return list(reversed(ops))


if __name__ == "__main__":
    pairs = [("kitten", "sitting"), ("sunday", "saturday"), ("", "abc")]
    for s1, s2 in pairs:
        print(f"  '{s1}' -> '{s2}': distance = {edit_distance(s1, s2)}")
    print(f"\nOperations for 'kitten' -> 'sitting':")
    for op in edit_operations("kitten", "sitting"):
        print(f"  {op}")
