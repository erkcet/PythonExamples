"""Find the longest palindromic substring."""


def longest_palindrome(s):
    """Find longest palindromic substring using expand-around-center."""
    if len(s) < 2:
        return s
    start, max_len = 0, 1

    def expand(left, right):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)       # Odd length palindromes
        expand(i, i + 1)   # Even length palindromes
    return s[start:start + max_len]


def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]


def count_palindromic_substrings(s):
    """Count all palindromic substrings."""
    count = 0
    for i in range(len(s)):
        for l, r in [(i, i), (i, i + 1)]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
    return count


if __name__ == "__main__":
    tests = ["babad", "cbbd", "racecar", "aacabdkacaa"]
    for t in tests:
        print(f"'{t}' -> longest palindrome: '{longest_palindrome(t)}'")
    print(f"\nPalindromic substrings in 'aaba': {count_palindromic_substrings('aaba')}")
