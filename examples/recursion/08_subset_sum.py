"""Subset Sum Problem.

Determines if a subset of the given set sums to a target value.
Uses recursive backtracking. Classic NP-complete problem.
"""


def has_subset_sum(arr: list, target: int) -> bool:
    """Check if any subset of arr sums to target."""
    return _subset_helper(arr, target, len(arr) - 1)


def _subset_helper(arr: list, target: int, idx: int) -> bool:
    """Recursive helper: include or exclude current element."""
    if target == 0:
        return True
    if idx < 0 or target < 0:
        return False
    if arr[idx] > target:
        return _subset_helper(arr, target, idx - 1)
    return (_subset_helper(arr, target - arr[idx], idx - 1) or
            _subset_helper(arr, target, idx - 1))


def find_subset_sum(arr: list, target: int) -> list:
    """Return a subset that sums to target, or empty list."""
    result = []
    def backtrack(idx, remaining, path):
        if remaining == 0:
            result.extend(path)
            return True
        if idx >= len(arr) or remaining < 0:
            return False
        if backtrack(idx + 1, remaining - arr[idx], path + [arr[idx]]):
            return True
        return backtrack(idx + 1, remaining, path)
    backtrack(0, target, [])
    return result


if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    for t in [9, 30, 100]:
        found = has_subset_sum(nums, t)
        subset = find_subset_sum(nums, t) if found else []
        print(f"Target {t:3d}: {'Yes':3s} -> {subset}" if found else f"Target {t:3d}: No")
