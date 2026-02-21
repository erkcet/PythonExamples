"""Selection Sort Algorithm.

Finds the minimum element from the unsorted part and puts it
at the beginning. O(n^2) time complexity.
"""


def selection_sort(arr: list) -> list:
    """Sort a list using selection sort algorithm."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print(f"Original: {data}")
    print(f"Sorted:   {selection_sort(data)}")
    print(f"Already sorted: {selection_sort([1, 2, 3, 4, 5])}")
