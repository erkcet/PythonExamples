"""Basic regex matching with re.match, re.search, and re.findall."""

import re


def demonstrate_match(pattern, text):
    """Try re.match (matches from start of string)."""
    result = re.match(pattern, text)
    return result.group() if result else None


def demonstrate_search(pattern, text):
    """Try re.search (finds first occurrence anywhere)."""
    result = re.search(pattern, text)
    return result.group() if result else None


def demonstrate_findall(pattern, text):
    """Find all non-overlapping matches in the string."""
    return re.findall(pattern, text)


if __name__ == "__main__":
    text = "The price is 42 dollars and 99 cents"

    print("match for digit at start:", demonstrate_match(r"\d+", text))
    print("match for 'The':", demonstrate_match(r"The", text))

    print("search for digit:", demonstrate_search(r"\d+", text))
    print("search for 'dollars':", demonstrate_search(r"dollars", text))

    print("findall digits:", demonstrate_findall(r"\d+", text))
    print("findall words:", demonstrate_findall(r"[a-zA-Z]+", text))
