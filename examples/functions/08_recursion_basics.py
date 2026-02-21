"""Basic recursion examples: factorial, sum, and tree traversal."""


def factorial(n):
    """Compute n! recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def recursive_sum(lst):
    """Sum a list recursively."""
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])


def flatten(nested):
    """Flatten an arbitrarily nested list."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def binary_search(arr, target, lo=0, hi=None):
    """Recursive binary search returning index or -1."""
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)
    return binary_search(arr, target, lo, mid - 1)


if __name__ == "__main__":
    print(f"5! = {factorial(5)}")
    print(f"sum([1,2,3,4]) = {recursive_sum([1, 2, 3, 4])}")
    print(f"flatten: {flatten([1, [2, [3, 4], 5], 6])}")
    print(f"search 7 in [1..9]: index {binary_search(list(range(1, 10)), 7)}")
