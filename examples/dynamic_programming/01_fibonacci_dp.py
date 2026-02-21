"""Fibonacci with Dynamic Programming.

Computes Fibonacci numbers using bottom-up tabulation and
space-optimized approaches. O(n) time.
"""


def fib_tabulation(n: int) -> int:
    """Compute nth Fibonacci using bottom-up DP table."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib_optimized(n: int) -> int:
    """Compute nth Fibonacci using O(1) space."""
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


if __name__ == "__main__":
    print("Fibonacci sequence (tabulation):")
    print([fib_tabulation(i) for i in range(15)])
    print(f"\nfib(50) = {fib_optimized(50)}")
    print(f"fib(100) = {fib_optimized(100)}")
