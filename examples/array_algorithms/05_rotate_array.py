"""Rotate array by k positions."""


def rotate_right(nums, k):
    """Rotate array to the right by k steps. O(n) time, O(1) space."""
    n = len(nums)
    k = k % n
    if k == 0:
        return nums
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums


def rotate_left(nums, k):
    """Rotate array to the left by k steps."""
    return rotate_right(nums, len(nums) - k)


def rotate_simple(nums, k):
    """Simple rotation using slicing (creates new list)."""
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(f"Original:      {arr}")
    print(f"Right by 3:    {rotate_simple(arr, 3)}")
    print(f"Left by 2:     {rotate_simple(arr, len(arr) - 2)}")
    arr2 = arr[:]
    rotate_right(arr2, 3)
    print(f"In-place right: {arr2}")
