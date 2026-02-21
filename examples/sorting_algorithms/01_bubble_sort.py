"""Bubble Sort Algorithm.

Repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order. O(n^2) time complexity.
"""


def bubble_sort(arr: list) -> list:
    """Sort a list using bubble sort algorithm."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {data}")
    print(f"Sorted:   {bubble_sort(data)}")
    print(f"Strings:  {bubble_sort(['banana', 'apple', 'cherry'])}")
