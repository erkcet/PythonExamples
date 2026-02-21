"""Quick Sort Algorithm.

Picks a pivot, partitions the array around it, and recursively
sorts the sub-arrays. O(n log n) average, O(n^2) worst case.
"""


def quick_sort(arr: list) -> list:
    """Sort a list using quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr: list, low: int = 0, high: int = None) -> None:
    """In-place quick sort using Lomuto partition scheme."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_val = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot_val:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print(f"Original:  {data}")
    print(f"Sorted:    {quick_sort(data)}")
    data2 = [10, 7, 8, 9, 1, 5]
    quick_sort_inplace(data2)
    print(f"In-place:  {data2}")
