"""Dutch National Flag problem: sort an array of 0s, 1s, and 2s."""


def dutch_flag_sort(arr):
    """Sort 0s, 1s, 2s in one pass using three pointers."""
    result = arr.copy()
    lo, mid, hi = 0, 0, len(result) - 1
    while mid <= hi:
        if result[mid] == 0:
            result[lo], result[mid] = result[mid], result[lo]
            lo += 1; mid += 1
        elif result[mid] == 1:
            mid += 1
        else:
            result[mid], result[hi] = result[hi], result[mid]
            hi -= 1
    return result


def three_way_partition(arr, pivot):
    """Partition array into <pivot, ==pivot, >pivot."""
    result = arr.copy()
    lo, mid, hi = 0, 0, len(result) - 1
    while mid <= hi:
        if result[mid] < pivot:
            result[lo], result[mid] = result[mid], result[lo]
            lo += 1; mid += 1
        elif result[mid] == pivot:
            mid += 1
        else:
            result[mid], result[hi] = result[hi], result[mid]
            hi -= 1
    return result


if __name__ == "__main__":
    arr = [2, 0, 1, 2, 1, 0, 0, 2, 1]
    print(f"Original: {arr}")
    print(f"Sorted:   {dutch_flag_sort(arr)}")
    data = [5, 3, 7, 3, 2, 8, 3, 1]
    print(f"Partition around 3: {three_way_partition(data, 3)}")
