"""Doctests embedded directly in function docstrings.

Run with: python -m doctest 03_doctest_examples.py -v
"""


def factorial(n):
    """Return n! for non-negative integers.

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(1)
    1
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def reverse_string(s):
    """Return the reversed string.

    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("")
    ''
    >>> reverse_string("a")
    'a'
    """
    return s[::-1]


if __name__ == "__main__":
    import doctest
    results = doctest.testmod(verbose=True)
    print(f"\n{results.attempted} tests, {results.failed} failures")
