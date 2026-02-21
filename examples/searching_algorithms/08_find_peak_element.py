"""Find Peak Element.

A peak element is greater than its neighbors. Uses binary search
to find a peak in O(log n) time.
"""


def find_peak(arr: list) -> int:
    """Return the index of any peak element."""
    if not arr:
        return -1
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low


def find_all_peaks(arr: list) -> list:
    """Return indices of all peak elements (linear scan)."""
    if not arr:
        return []
    peaks = []
    n = len(arr)
    for i in range(n):
        left_ok = (i == 0) or (arr[i] >= arr[i - 1])
        right_ok = (i == n - 1) or (arr[i] >= arr[i + 1])
        if left_ok and right_ok:
            peaks.append(i)
    return peaks


if __name__ == "__main__":
    data = [1, 3, 20, 4, 1, 0, 6, 2]
    peak_idx = find_peak(data)
    print(f"Array: {data}")
    print(f"A peak: index {peak_idx}, value {data[peak_idx]}")
    all_peaks = find_all_peaks(data)
    print(f"All peaks: {[(i, data[i]) for i in all_peaks]}")
