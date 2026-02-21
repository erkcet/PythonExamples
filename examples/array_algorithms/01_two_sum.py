"""Two Sum: find two numbers that add up to a target."""


def two_sum(nums, target):
    """Return indices of two numbers that add up to target. O(n) time."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def two_sum_sorted(nums, target):
    """Two sum for a sorted array using two pointers. O(n) time, O(1) space."""
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


def two_sum_all_pairs(nums, target):
    """Find all unique pairs that sum to target."""
    seen, pairs = set(), set()
    for num in nums:
        comp = target - num
        if comp in seen:
            pairs.add((min(num, comp), max(num, comp)))
        seen.add(num)
    return list(pairs)


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    print(f"two_sum({nums}, 9) = {two_sum(nums, 9)}")
    print(f"two_sum_sorted({nums}, 18) = {two_sum_sorted(nums, 18)}")
    nums2 = [1, 3, 2, 4, 3, 5]
    print(f"all pairs summing to 6: {two_sum_all_pairs(nums2, 6)}")
