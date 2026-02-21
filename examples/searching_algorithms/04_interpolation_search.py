"""Interpolation Search Algorithm.

Estimates the position of the target based on its value relative
to the range. O(log log n) for uniform distributions, O(n) worst.
"""


def interpolation_search(arr: list, target) -> int:
    """Search for target using interpolation of values."""
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if arr[low] == arr[high]:
            return low if arr[low] == target else -1
        pos = low + ((target - arr[low]) * (high - low)
                      // (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1


if __name__ == "__main__":
    data = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    print(f"Search 18: index {interpolation_search(data, 18)}")
    print(f"Search 33: index {interpolation_search(data, 33)}")
    print(f"Search 99: index {interpolation_search(data, 99)}")
