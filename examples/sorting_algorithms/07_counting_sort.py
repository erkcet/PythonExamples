"""Counting Sort Algorithm.

Counts occurrences of each value and reconstructs the sorted array.
O(n + k) time where k is the range of input values.
"""


def counting_sort(arr: list) -> list:
    """Sort a list of non-negative integers using counting sort."""
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for val, cnt in enumerate(count):
        result.extend([val] * cnt)
    return result


def counting_sort_stable(arr: list) -> list:
    """Stable counting sort preserving relative order."""
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num] -= 1
        output[count[num]] = num
    return output


if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print(f"Original: {data}")
    print(f"Sorted:   {counting_sort(data)}")
    print(f"Stable:   {counting_sort_stable(data)}")
