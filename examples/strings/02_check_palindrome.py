"""Check whether a given string is a palindrome."""


def is_palindrome(s):
    """Return True if s reads the same forwards and backwards (case-insensitive)."""
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    words = ["racecar", "hello", "A man a plan a canal Panama", "Madam", "python"]
    for word in words:
        result = is_palindrome(word)
        print(f"'{word}' -> palindrome: {result}")
