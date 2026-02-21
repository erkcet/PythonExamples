"""Merge overlapping intervals."""


def merge_intervals(intervals):
    """Merge all overlapping intervals. O(n log n)."""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def insert_interval(intervals, new):
    """Insert a new interval and merge if necessary."""
    intervals.append(new)
    return merge_intervals(intervals)


def interval_intersection(a, b):
    """Find the intersection of two lists of intervals."""
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        lo = max(a[i][0], b[j][0])
        hi = min(a[i][1], b[j][1])
        if lo <= hi:
            result.append([lo, hi])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return result


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Input:    {intervals}")
    print(f"Merged:   {merge_intervals(intervals)}")
    print(f"Insert [4,9]: {insert_interval([[1,3],[6,9]], [4,5])}")
    a = [[0,2],[5,10],[13,23]]
    b = [[1,5],[8,12],[15,24]]
    print(f"Intersection: {interval_intersection(a, b)}")
