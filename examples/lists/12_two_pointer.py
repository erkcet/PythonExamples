"""Two pointer technique on sorted lists."""


def two_sum_sorted(arr, target):
    """Find pair summing to target in a sorted array."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return (lo, hi)
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return None


def remove_duplicates_inplace(arr):
    """Remove duplicates in sorted array, return new length."""
    if not arr:
        return 0
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1
    return write


def is_palindrome(s):
    """Check palindrome using two pointers, ignoring non-alnum."""
    lo, hi = 0, len(s) - 1
    while lo < hi:
        while lo < hi and not s[lo].isalnum():
            lo += 1
        while lo < hi and not s[hi].isalnum():
            hi -= 1
        if s[lo].lower() != s[hi].lower():
            return False
        lo, hi = lo + 1, hi - 1
    return True


if __name__ == "__main__":
    arr = [1, 2, 4, 6, 8, 10]
    print(f"Two sum (target=10): indices {two_sum_sorted(arr, 10)}")
    dup = [1, 1, 2, 2, 3, 4, 4, 5]
    length = remove_duplicates_inplace(dup)
    print(f"Deduped: {dup[:length]}")
    print(f"'A man, a plan, a canal: Panama' -> {is_palindrome('A man, a plan, a canal: Panama')}")
