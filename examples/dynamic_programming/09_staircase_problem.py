"""Climbing Stairs Problem.

Count the number of distinct ways to reach the top of a staircase
with n steps, taking 1 or 2 steps at a time. O(n) time.
"""


def climb_stairs(n: int) -> int:
    """Return number of ways to climb n stairs (1 or 2 steps)."""
    if n <= 2:
        return max(n, 0)
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


def climb_stairs_k_steps(n: int, k: int) -> int:
    """Return number of ways to climb n stairs taking 1..k steps."""
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for step in range(1, min(k, i) + 1):
            dp[i] += dp[i - step]
    return dp[n]


def climb_stairs_min_cost(cost: list) -> int:
    """Return min cost to reach the top. Start from step 0 or 1."""
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]


if __name__ == "__main__":
    for n in range(1, 11):
        print(f"Stairs={n}: {climb_stairs(n)} ways")
    print(f"\n5 stairs, up to 3 steps: {climb_stairs_k_steps(5, 3)} ways")
    cost = [10, 15, 20]
    print(f"Min cost for {cost}: {climb_stairs_min_cost(cost)}")
