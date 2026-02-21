"""Bucket Sort Algorithm.

Distributes elements into buckets, sorts each bucket individually,
then concatenates. O(n + k) average time for uniform distributions.
"""


def bucket_sort(arr: list, bucket_count: int = 10) -> list:
    """Sort a list of floats in [0, 1) using bucket sort."""
    if not arr:
        return []
    buckets = [[] for _ in range(bucket_count)]
    for val in arr:
        idx = int(val * bucket_count)
        idx = min(idx, bucket_count - 1)
        buckets[idx].append(val)
    for bucket in buckets:
        bucket.sort()
    return [val for bucket in buckets for val in bucket]


def bucket_sort_integers(arr: list, bucket_size: int = 5) -> list:
    """Sort integers using bucket sort."""
    if not arr:
        return []
    min_val, max_val = min(arr), max(arr)
    count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(count)]
    for val in arr:
        buckets[(val - min_val) // bucket_size].append(val)
    for bucket in buckets:
        bucket.sort()
    return [v for b in buckets for v in b]


if __name__ == "__main__":
    floats = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    print(f"Floats:   {bucket_sort(floats)}")
    ints = [29, 25, 3, 49, 9, 37, 21, 43]
    print(f"Integers: {bucket_sort_integers(ints)}")
