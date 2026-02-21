"""Ternary Search Algorithm.

Divides the search space into three parts instead of two.
O(log3 n) time complexity. Works on sorted arrays.
"""


def ternary_search(arr: list, target) -> int:
    """Search for target using ternary search on a sorted array."""
    low, high = 0, len(arr) - 1
    while low <= high:
        third = (high - low) // 3
        mid1 = low + third
        mid2 = high - third
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for val in [1, 6, 12, 13]:
        idx = ternary_search(data, val)
        status = f"index {idx}" if idx != -1 else "not found"
        print(f"Search {val:2d}: {status}")
