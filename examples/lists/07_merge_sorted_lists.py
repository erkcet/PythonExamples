"""Merge two sorted lists into one sorted list."""

from heapq import merge as heapmerge


def merge_two_pointer(a, b):
    """Merge two sorted lists with two pointers (O(n+m))."""
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def merge_heapq(a, b):
    """Merge using heapq.merge (supports multiple iterables)."""
    return list(heapmerge(a, b))


def merge_k_lists(lists):
    """Merge k sorted lists using heapq."""
    return list(heapmerge(*lists))


if __name__ == "__main__":
    a, b = [1, 3, 5, 7], [2, 4, 6, 8]
    print(f"Two-pointer: {merge_two_pointer(a, b)}")
    print(f"Heapq:       {merge_heapq(a, b)}")
    k_lists = [[1, 5, 9], [2, 6, 10], [3, 7, 11]]
    print(f"K-way merge: {merge_k_lists(k_lists)}")
