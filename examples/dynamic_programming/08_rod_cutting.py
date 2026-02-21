"""Rod Cutting Problem.

Given a rod of length n and a table of prices for each length,
determine the maximum revenue from cutting the rod. O(n^2).
"""


def rod_cutting(prices: list, length: int) -> int:
    """Return maximum revenue obtainable by cutting a rod."""
    dp = [0] * (length + 1)
    for i in range(1, length + 1):
        for j in range(1, i + 1):
            if j <= len(prices):
                dp[i] = max(dp[i], prices[j - 1] + dp[i - j])
    return dp[length]


def rod_cutting_with_cuts(prices: list, length: int) -> tuple:
    """Return (max_revenue, list_of_cut_lengths)."""
    dp = [0] * (length + 1)
    first_cut = [0] * (length + 1)
    for i in range(1, length + 1):
        for j in range(1, i + 1):
            if j <= len(prices) and prices[j - 1] + dp[i - j] > dp[i]:
                dp[i] = prices[j - 1] + dp[i - j]
                first_cut[i] = j
    cuts = []
    remaining = length
    while remaining > 0:
        cuts.append(first_cut[remaining])
        remaining -= first_cut[remaining]
    return dp[length], cuts


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    for n in [4, 8]:
        revenue, cuts = rod_cutting_with_cuts(prices, n)
        print(f"Rod length {n}: max revenue = {revenue}, cuts = {cuts}")
