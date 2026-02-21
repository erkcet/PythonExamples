"""Demonstrate multiple ways to reverse a string in Python."""


def reverse_string(s):
    """Reverse a string using slicing."""
    return s[::-1]


def reverse_string_loop(s):
    """Reverse a string using a loop."""
    result = ""
    for char in s:
        result = char + result
    return result


if __name__ == "__main__":
    test = "Hello, World!"
    print(f"Original:       {test}")
    print(f"Slicing:        {reverse_string(test)}")
    print(f"Loop:           {reverse_string_loop(test)}")
    print(f"Reversed built-in: {''.join(reversed(test))}")
