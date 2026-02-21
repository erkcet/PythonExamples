"""Remove duplicate characters from a string while preserving order."""


def remove_duplicates(s):
    """Return string with only the first occurrence of each character."""
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)


if __name__ == "__main__":
    tests = ["programming", "abracadabra", "hello world", "aabbccdd"]
    for t in tests:
        print(f"'{t}' -> '{remove_duplicates(t)}'")
