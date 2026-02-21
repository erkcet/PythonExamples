"""Three Sum: find all unique triplets that sum to zero."""


def three_sum(nums, target=0):
    """Find all unique triplets that sum to target. O(n^2) time."""
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return result


def three_sum_closest(nums, target):
    """Find the triplet sum closest to target."""
    nums.sort()
    closest = float("inf")
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(closest - target):
                closest = total
            if total < target:
                left += 1
            else:
                right -= 1
    return closest


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"three_sum({nums}) = {three_sum(nums[:])}")
    print(f"closest to 1: {three_sum_closest(nums[:], 1)}")
