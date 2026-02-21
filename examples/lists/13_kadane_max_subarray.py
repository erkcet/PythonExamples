"""Kadane's algorithm for maximum subarray sum."""


def max_subarray_sum(arr):
    """Return the maximum subarray sum."""
    max_ending = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far


def max_subarray_with_indices(arr):
    """Return max subarray sum along with start and end indices."""
    max_sum = cur_sum = arr[0]
    start = end = temp_start = 0
    for i in range(1, len(arr)):
        if arr[i] > cur_sum + arr[i]:
            cur_sum = arr[i]
            temp_start = i
        else:
            cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            start, end = temp_start, i
    return max_sum, start, end


def max_circular_subarray(arr):
    """Maximum subarray sum considering circular wraparound."""
    max_kadane = max_subarray_sum(arr)
    total = sum(arr)
    inverted = [-x for x in arr]
    max_inverted = max_subarray_sum(inverted)
    max_circular = total + max_inverted
    if max_circular == 0:
        return max_kadane
    return max(max_kadane, max_circular)


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {arr}")
    print(f"Max subarray sum: {max_subarray_sum(arr)}")
    s, i, j = max_subarray_with_indices(arr)
    print(f"Sum={s}, subarray={arr[i:j+1]}")
    circ = [5, -3, 5]
    print(f"Circular max ({circ}): {max_circular_subarray(circ)}")
