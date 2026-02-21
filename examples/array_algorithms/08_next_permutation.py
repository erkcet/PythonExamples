"""Next permutation of an array."""


def next_permutation(nums):
    """Rearrange to next lexicographically greater permutation. In-place, O(n)."""
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


def all_permutations(nums):
    """Generate all permutations in lexicographic order."""
    nums = sorted(nums)
    perms = [nums[:]]
    while True:
        nums = next_permutation(nums[:])
        if nums == perms[0]:
            break
        perms.append(nums[:])
    return perms


def prev_permutation(nums):
    """Find the previous lexicographic permutation."""
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] <= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] >= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(f"All permutations of {arr}:")
    for p in all_permutations(arr):
        print(f"  {p}")
    test = [1, 3, 2]
    print(f"\nNext of {test}: {next_permutation(test[:])}")
    print(f"Prev of [1,3,2]: {prev_permutation([1,3,2])}")
