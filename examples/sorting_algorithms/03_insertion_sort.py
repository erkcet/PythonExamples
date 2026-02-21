"""Insertion Sort Algorithm.

Builds the sorted array one item at a time by inserting each
element into its correct position. O(n^2) time, O(n) best case.
"""


def insertion_sort(arr: list) -> list:
    """Sort a list using insertion sort algorithm."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print(f"Original: {data}")
    print(f"Sorted:   {insertion_sort(data)}")
    nearly = [1, 2, 4, 3, 5]
    print(f"Nearly sorted {nearly} -> {insertion_sort(nearly)}")
