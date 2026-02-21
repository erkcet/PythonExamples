"""Recursive Binary Search.

Searches a sorted array by recursively halving the search space.
O(log n) time, O(log n) stack space.
"""


def binary_search(arr: list, target, low: int = 0, high: int = None) -> int:
    """Recursively search for target in sorted arr. Returns index or -1."""
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)


def binary_search_first(arr: list, target, low: int = 0, high: int = None) -> int:
    """Find the first occurrence of target in a sorted array."""
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target and (mid == 0 or arr[mid - 1] != target):
        return mid
    elif arr[mid] < target:
        return binary_search_first(arr, target, mid + 1, high)
    else:
        return binary_search_first(arr, target, low, mid - 1)


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13, 15]
    for val in [7, 1, 15, 6]:
        idx = binary_search(data, val)
        print(f"Search {val:2d}: {'found at ' + str(idx) if idx != -1 else 'not found'}")
    dupes = [1, 2, 2, 2, 3, 4]
    print(f"\nFirst occurrence of 2 in {dupes}: index {binary_search_first(dupes, 2)}")
