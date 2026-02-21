"""Generate Combinations Recursively.

Generates all C(n, k) combinations of choosing k elements from n.
Uses backtracking to build combinations.
"""


def combinations(arr: list, k: int) -> list:
    """Generate all combinations of k elements from arr."""
    result = []
    _combine(arr, k, 0, [], result)
    return result


def _combine(arr, k, start, current, result):
    """Backtracking helper for combination generation."""
    if len(current) == k:
        result.append(current[:])
        return
    for i in range(start, len(arr)):
        current.append(arr[i])
        _combine(arr, k, i + 1, current, result)
        current.pop()  # backtrack


def combination_sum(candidates: list, target: int) -> list:
    """Find all combinations that sum to target (elements reusable)."""
    result = []
    candidates.sort()
    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)
            path.pop()
    backtrack(0, target, [])
    return result


if __name__ == "__main__":
    print("C([1,2,3,4], 2):")
    for c in combinations([1, 2, 3, 4], 2):
        print(f"  {c}")
    print(f"\nCombinations summing to 7: {combination_sum([2, 3, 6, 7], 7)}")
