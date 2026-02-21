"""Check if a number is a palindrome."""


def is_palindrome(n: int) -> bool:
    """Return True if n reads the same forwards and backwards."""
    s = str(abs(n))
    return s == s[::-1]


def is_palindrome_numeric(n: int) -> bool:
    """Check palindrome without string conversion."""
    if n < 0:
        return False
    original, reversed_num = n, 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return original == reversed_num


def find_palindromes(start: int, end: int) -> list[int]:
    """Find all palindrome numbers in a range."""
    return [n for n in range(start, end + 1) if is_palindrome(n)]


if __name__ == "__main__":
    test_nums = [121, 123, 1331, 12321, 45654, 12345]
    for num in test_nums:
        status = "is" if is_palindrome(num) else "is not"
        print(f"{num:>6} {status} a palindrome")
    print(f"\nPalindromes 100-200: {find_palindromes(100, 200)}")
