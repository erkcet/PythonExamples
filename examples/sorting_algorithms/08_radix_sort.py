"""Radix Sort Algorithm.

Sorts integers by processing individual digits from least significant
to most significant. O(d * (n + k)) time where d is digit count.
"""


def radix_sort(arr: list) -> list:
    """Sort non-negative integers using LSD radix sort."""
    if not arr:
        return []
    arr = arr.copy()
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = _counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr


def _counting_sort_by_digit(arr: list, exp: int) -> list:
    """Sort array by a specific digit position."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for num in reversed(arr):
        digit = (num // exp) % 10
        count[digit] -= 1
        output[count[digit]] = num
    return output


if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Original: {data}")
    print(f"Sorted:   {radix_sort(data)}")
