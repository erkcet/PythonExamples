"""Coin Change Problem.

Find the minimum number of coins needed to make a given amount.
O(amount * n) time where n is the number of coin denominations.
"""


def coin_change(coins: list, amount: int) -> int:
    """Return minimum coins needed, or -1 if impossible."""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
    return dp[amount] if dp[amount] != float("inf") else -1


def coin_change_ways(coins: list, amount: int) -> int:
    """Return the number of ways to make the amount."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]


if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    for amt in [11, 30, 3]:
        min_c = coin_change(coins, amt)
        ways = coin_change_ways(coins, amt)
        print(f"Amount {amt:2d}: min coins = {min_c}, ways = {ways}")
