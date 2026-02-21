"""Search in Rotated Sorted Array.

Finds a target in a sorted array that has been rotated at some pivot.
Uses modified binary search. O(log n) time complexity.
"""


def search_rotated(arr: list, target) -> int:
    """Search for target in a rotated sorted array."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:  # Left half is sorted
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def find_rotation_point(arr: list) -> int:
    """Find the index of the minimum element (rotation point)."""
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == "__main__":
    data = [15, 18, 2, 3, 6, 12]
    print(f"Array: {data}")
    print(f"Search 3:  index {search_rotated(data, 3)}")
    print(f"Search 18: index {search_rotated(data, 18)}")
    print(f"Rotation point: index {find_rotation_point(data)}")
