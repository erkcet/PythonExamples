"""Heap Sort Algorithm.

Builds a max-heap from the array, then repeatedly extracts the
maximum element. O(n log n) time complexity, in-place.
"""


def heap_sort(arr: list) -> list:
    """Sort a list using heap sort algorithm."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    return arr


def _heapify(arr: list, size: int, root: int) -> None:
    """Maintain the max-heap property for a subtree."""
    largest = root
    left, right = 2 * root + 1, 2 * root + 2
    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        _heapify(arr, size, largest)


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print(f"Original: {data}")
    print(f"Sorted:   {heap_sort(data)}")
