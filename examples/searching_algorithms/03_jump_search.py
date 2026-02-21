"""Jump Search Algorithm.

Searches a sorted array by jumping ahead fixed steps, then
performing linear search in the block. O(sqrt(n)) time.
"""

import math


def jump_search(arr: list, target) -> int:
    """Search for target in sorted arr using jump search."""
    n = len(arr)
    if n == 0:
        return -1
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    data = list(range(0, 100, 3))  # [0, 3, 6, ..., 99]
    print(f"Array: {data[:10]}... (len={len(data)})")
    print(f"Search 24: index {jump_search(data, 24)}")
    print(f"Search 25: index {jump_search(data, 25)}")
