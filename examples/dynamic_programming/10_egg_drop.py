"""Egg Drop Puzzle.

Given k eggs and n floors, find the minimum number of trials
needed in the worst case to determine the critical floor.
"""


def egg_drop(eggs: int, floors: int) -> int:
    """Return minimum trials needed using O(k*n^2) DP."""
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]
    for j in range(1, floors + 1):
        dp[1][j] = j  # 1 egg: linear search
    for i in range(1, eggs + 1):
        dp[i][0] = 0
        dp[i][1] = 1
    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            dp[i][j] = float("inf")
            for x in range(1, j + 1):
                worst = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                dp[i][j] = min(dp[i][j], worst)
    return dp[eggs][floors]


def egg_drop_optimized(eggs: int, floors: int) -> int:
    """Find min trials using the inverse approach. O(k * log n)."""
    if floors <= 1:
        return floors
    dp = [[0] * (eggs + 1) for _ in range(floors + 1)]
    trial = 0
    while dp[trial][eggs] < floors:
        trial += 1
        for e in range(1, eggs + 1):
            dp[trial][e] = dp[trial - 1][e - 1] + dp[trial - 1][e] + 1
    return trial


if __name__ == "__main__":
    test_cases = [(1, 10), (2, 10), (2, 36), (3, 100)]
    for k, n in test_cases:
        result = egg_drop(k, n)
        opt = egg_drop_optimized(k, n)
        print(f"{k} egg(s), {n:3d} floors: {result} trials (optimized: {opt})")
