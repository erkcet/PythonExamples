"""Find the majority element (appears more than n/2 times)."""

from collections import Counter


def majority_element_boyer_moore(nums):
    """Boyer-Moore Voting Algorithm. O(n) time, O(1) space."""
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


def majority_element_counter(nums):
    """Find majority element using Counter."""
    counts = Counter(nums)
    threshold = len(nums) // 2
    for num, count in counts.items():
        if count > threshold:
            return num
    return None


def majority_elements_k(nums, k):
    """Find all elements appearing more than n/k times."""
    counts = Counter(nums)
    threshold = len(nums) // k
    return [num for num, count in counts.items() if count > threshold]


if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]
    print(f"Array: {arr}")
    print(f"Majority (Boyer-Moore): {majority_element_boyer_moore(arr)}")
    print(f"Majority (Counter):     {majority_element_counter(arr)}")
    arr2 = [3, 2, 3, 1, 2, 3, 2]
    print(f"\nElements appearing > n/3 times: {majority_elements_k(arr2, 3)}")
