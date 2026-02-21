"""Find all pairs in a list that sum to a target using sets."""


def find_pair(arr, target):
    """Find one pair summing to target (O(n) with set)."""
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None


def find_all_pairs(arr, target):
    """Find all unique pairs summing to target."""
    seen, used, pairs = set(), set(), []
    for num in arr:
        complement = target - num
        pair = (min(num, complement), max(num, complement))
        if complement in seen and pair not in used:
            pairs.append(pair)
            used.add(pair)
        seen.add(num)
    return pairs


def count_pairs(arr, target):
    """Count the number of pairs summing to target."""
    from collections import Counter
    counts = Counter(arr)
    total = 0
    for num in counts:
        comp = target - num
        if comp in counts:
            if comp == num:
                total += counts[num] * (counts[num] - 1) // 2
            elif comp > num:
                total += counts[num] * counts[comp]
    return total


if __name__ == "__main__":
    arr = [2, 4, 3, 5, 7, 8, 1, 6]
    print(f"First pair for sum=9: {find_pair(arr, 9)}")
    print(f"All pairs for sum=9:  {find_all_pairs(arr, 9)}")
    arr2 = [1, 5, 7, -1, 5]
    print(f"Count pairs sum=6:    {count_pairs(arr2, 6)}")
