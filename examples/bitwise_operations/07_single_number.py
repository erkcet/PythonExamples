"""Find the single number in an array using XOR trick."""


def single_number(nums: list[int]) -> int:
    """Find the element that appears once; all others appear twice.

    XOR of a number with itself is 0, and XOR with 0 is the number.
    """
    result = 0
    for n in nums:
        result ^= n
    return result


def two_single_numbers(nums: list[int]) -> tuple[int, int]:
    """Find two elements that each appear once; others appear twice."""
    xor_all = 0
    for n in nums:
        xor_all ^= n
    # Find rightmost set bit to split into two groups
    diff_bit = xor_all & (-xor_all)
    a, b = 0, 0
    for n in nums:
        if n & diff_bit:
            a ^= n
        else:
            b ^= n
    return (min(a, b), max(a, b))


if __name__ == "__main__":
    arr1 = [2, 3, 5, 4, 5, 3, 4]
    print(f"Array: {arr1}")
    print(f"Single number: {single_number(arr1)}")

    arr2 = [1, 2, 1, 3, 2, 5]
    print(f"\nArray: {arr2}")
    print(f"Two singles: {two_single_numbers(arr2)}")
