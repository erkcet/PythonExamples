"""Catalan numbers and their applications."""

from math import comb


def catalan_formula(n):
    """Compute nth Catalan number using the binomial formula."""
    return comb(2 * n, n) // (n + 1)


def catalan_dp(n):
    """Compute nth Catalan number using dynamic programming."""
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = sum(dp[j] * dp[i - 1 - j] for j in range(i))
    return dp[n]


def catalan_sequence(count):
    """Generate the first 'count' Catalan numbers."""
    return [catalan_formula(i) for i in range(count)]


def catalan_applications(n):
    """Show what the nth Catalan number counts."""
    c = catalan_formula(n)
    return {
        "balanced_parentheses": f"{c} ways to arrange {n} pairs",
        "binary_trees": f"{c} distinct binary trees with {n} nodes",
        "triangulations": f"{c} ways to triangulate a {n+2}-gon",
    }


if __name__ == "__main__":
    print(f"First 12 Catalan numbers: {catalan_sequence(12)}")
    print(f"C(10) formula: {catalan_formula(10)}")
    print(f"C(10) dp:      {catalan_dp(10)}")
    print(f"\nApplications of C(5):")
    for k, v in catalan_applications(5).items():
        print(f"  {k}: {v}")
