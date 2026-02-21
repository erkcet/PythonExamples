"""Longest Increasing Subsequence (LIS).

Finds the longest strictly increasing subsequence in an array.
O(n^2) DP approach and O(n log n) optimized approach.
"""

import bisect


def lis_length(arr: list) -> int:
    """Return the length of LIS using O(n^2) DP."""
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_fast(arr: list) -> int:
    """Return LIS length using O(n log n) patience sorting."""
    tails = []
    for val in arr:
        pos = bisect.bisect_left(tails, val)
        if pos == len(tails):
            tails.append(val)
        else:
            tails[pos] = val
    return len(tails)


def lis_sequence(arr: list) -> list:
    """Return one actual LIS."""
    if not arr:
        return []
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    idx = dp.index(max(dp))
    seq = []
    while idx != -1:
        seq.append(arr[idx]); idx = parent[idx]
    return seq[::-1]


if __name__ == "__main__":
    data = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Array: {data}")
    print(f"LIS length (DP):   {lis_length(data)}")
    print(f"LIS length (fast): {lis_fast(data)}")
    print(f"LIS sequence:      {lis_sequence(data)}")
