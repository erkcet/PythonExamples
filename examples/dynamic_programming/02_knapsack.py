"""0/1 Knapsack Problem.

Given items with weights and values, maximize the total value
that fits in a knapsack of given capacity. O(n*W) time.
"""


def knapsack(weights: list, values: list, capacity: int) -> int:
    """Solve 0/1 knapsack and return maximum value."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]


def knapsack_items(weights: list, values: list, capacity: int) -> tuple:
    """Return (max_value, list_of_chosen_indices)."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
    items, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= weights[i - 1]
    return dp[n][capacity], items[::-1]


if __name__ == "__main__":
    W = [2, 3, 4, 5]
    V = [3, 4, 5, 6]
    cap = 8
    val, chosen = knapsack_items(W, V, cap)
    print(f"Weights: {W}, Values: {V}, Capacity: {cap}")
    print(f"Max value: {val}, Items: {chosen}")
