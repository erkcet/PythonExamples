"""Binary Search Algorithm (Iterative and Recursive).

Searches a sorted array by repeatedly dividing the search interval
in half. O(log n) time complexity.
"""


def binary_search_iterative(arr: list, target) -> int:
    """Iterative binary search. Returns index or -1."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr: list, target, low: int = 0, high: int = None) -> int:
    """Recursive binary search. Returns index or -1."""
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Iterative - search 23: index {binary_search_iterative(data, 23)}")
    print(f"Recursive - search 23: index {binary_search_recursive(data, 23)}")
    print(f"Search 99: index {binary_search_iterative(data, 99)}")
