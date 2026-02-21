"""Rotate a list by k positions."""


def rotate_right_slice(lst, k):
    """Rotate right by k using slicing."""
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


def rotate_left_slice(lst, k):
    """Rotate left by k using slicing."""
    if not lst:
        return lst
    k = k % len(lst)
    return lst[k:] + lst[:k]


def rotate_reverse(lst, k):
    """Rotate right using the reversal algorithm (in-place)."""
    n = len(lst)
    k = k % n
    result = lst.copy()

    def reverse(arr, lo, hi):
        while lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo, hi = lo + 1, hi - 1

    reverse(result, 0, n - 1)
    reverse(result, 0, k - 1)
    reverse(result, k, n - 1)
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(f"Original:        {nums}")
    print(f"Right by 3:      {rotate_right_slice(nums, 3)}")
    print(f"Left by 2:       {rotate_left_slice(nums, 2)}")
    print(f"Reversal (R by 3): {rotate_reverse(nums, 3)}")
