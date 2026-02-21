"""Product of array except self without division."""


def product_except_self(nums):
    """Compute product of all elements except self. O(n) time, O(n) space."""
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


def product_except_self_with_division(nums):
    """Product except self using division (handles zeros)."""
    zeros = nums.count(0)
    if zeros > 1:
        return [0] * len(nums)
    total = 1
    for x in nums:
        if x != 0:
            total *= x
    if zeros == 1:
        return [total if x == 0 else 0 for x in nums]
    return [total // x for x in nums]


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(f"Array:           {arr}")
    print(f"Product (no div): {product_except_self(arr)}")
    print(f"Product (div):    {product_except_self_with_division(arr)}")
    arr2 = [0, 1, 2, 3]
    print(f"\nWith zero {arr2}: {product_except_self(arr2)}")
