"""Sliding window technique on lists."""

from collections import deque


def max_sum_window(arr, k):
    """Find maximum sum of a subarray of size k."""
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def sliding_window_max(arr, k):
    """Find maximum in each window of size k using deque."""
    dq, result = deque(), []
    for i, val in enumerate(arr):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and arr[dq[-1]] < val:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result


def longest_unique_substring(s):
    """Find longest substring without repeating characters."""
    seen, start, max_len = {}, 0, 0
    for end, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = end
        max_len = max(max_len, end - start + 1)
    return max_len


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    print(f"Max sum (k=3): {max_sum_window(arr, 3)}")
    arr2 = [1, 3, -1, -3, 5, 3, 6, 7]
    print(f"Window max (k=3): {sliding_window_max(arr2, 3)}")
    print(f"Longest unique in 'abcabcbb': {longest_unique_substring('abcabcbb')}")
