"""Maximum subarray sum using Kadane's algorithm."""


def max_subarray(nums):
    """Find the contiguous subarray with the largest sum. O(n)."""
    max_sum = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum


def max_subarray_with_indices(nums):
    """Return max sum along with start and end indices."""
    max_sum = current = nums[0]
    start = end = temp_start = 0
    for i in range(1, len(nums)):
        if nums[i] > current + nums[i]:
            current = nums[i]
            temp_start = i
        else:
            current += nums[i]
        if current > max_sum:
            max_sum = current
            start, end = temp_start, i
    return max_sum, start, end


def max_circular_subarray(nums):
    """Max subarray sum in a circular array."""
    max_kadane = max_subarray(nums)
    total = sum(nums)
    inverted = [-x for x in nums]
    min_kadane = max_subarray(inverted)
    if total + min_kadane == 0:
        return max_kadane
    return max(max_kadane, total + min_kadane)


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {arr}")
    print(f"Max subarray sum: {max_subarray(arr)}")
    s, start, end = max_subarray_with_indices(arr)
    print(f"Subarray [{start}:{end+1}] = {arr[start:end+1]}, sum = {s}")
    print(f"Circular max: {max_circular_subarray([5, -3, 5])}")
