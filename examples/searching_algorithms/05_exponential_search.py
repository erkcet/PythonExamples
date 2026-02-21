"""Exponential Search Algorithm.

Finds the range where the target may exist by doubling the index,
then performs binary search within that range. O(log n) time.
"""


def exponential_search(arr: list, target) -> int:
    """Search for target using exponential search."""
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0
    bound = 1
    while bound < n and arr[bound] <= target:
        bound *= 2
    low = bound // 2
    high = min(bound, n - 1)
    return _binary_search(arr, target, low, high)


def _binary_search(arr: list, target, low: int, high: int) -> int:
    """Binary search within bounds."""
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    data = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
    print(f"Search 10:  index {exponential_search(data, 10)}")
    print(f"Search 100: index {exponential_search(data, 100)}")
    print(f"Search 5:   index {exponential_search(data, 5)}")
