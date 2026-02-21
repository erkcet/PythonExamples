"""Linear Search Algorithm.

Sequentially checks each element until a match is found or the
list is exhausted. O(n) time complexity.
"""


def linear_search(arr: list, target) -> int:
    """Return the index of target in arr, or -1 if not found."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def linear_search_all(arr: list, target) -> list:
    """Return all indices where target appears in arr."""
    return [i for i, val in enumerate(arr) if val == target]


if __name__ == "__main__":
    data = [10, 23, 45, 70, 11, 15, 70]
    print(f"Search 70: index {linear_search(data, 70)}")
    print(f"Search 99: index {linear_search(data, 99)}")
    print(f"All 70s:   indices {linear_search_all(data, 70)}")
