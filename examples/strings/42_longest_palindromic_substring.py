"""Find the longest palindromic substring in a given string."""


def longest_palindrome(s):
    """Return the longest palindromic substring using expand-around-center."""
    if len(s) < 2:
        return s

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    best = ""
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        candidate = odd if len(odd) > len(even) else even
        if len(candidate) > len(best):
            best = candidate
    return best


if __name__ == "__main__":
    tests = ["babad", "cbbd", "racecar", "a", "forgeeksskeegfor"]
    for t in tests:
        print(f"'{t}' -> longest palindrome: '{longest_palindrome(t)}'")
