"""Wildcard pattern matching with '?' and '*'."""


def wildcard_match(text, pattern):
    """Match text against pattern with ? (any char) and * (any sequence)."""
    m, n = len(text), len(pattern)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if pattern[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif pattern[j - 1] == "?" or text[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]


def simple_glob(text, pattern):
    """Simple glob matching (iterative approach)."""
    ti, pi, star, match = 0, 0, -1, 0
    while ti < len(text):
        if pi < len(pattern) and (pattern[pi] == "?" or pattern[pi] == text[ti]):
            ti, pi = ti + 1, pi + 1
        elif pi < len(pattern) and pattern[pi] == "*":
            star, match, pi = pi, ti, pi + 1
        elif star >= 0:
            match += 1
            ti, pi = match, star + 1
        else:
            return False
    while pi < len(pattern) and pattern[pi] == "*":
        pi += 1
    return pi == len(pattern)


if __name__ == "__main__":
    tests = [("hello", "h*o", True), ("cat", "c?t", True), ("abc", "a*d", False),
             ("abcde", "*c*e", True), ("", "*", True)]
    for text, pat, expected in tests:
        result = wildcard_match(text, pat)
        status = "ok" if result == expected else "FAIL"
        print(f"  [{status}] '{text}' ~ '{pat}' = {result}")
