"""Find all occurrences of a substring within a string."""


def find_all(text, sub):
    """Return a list of starting indices where sub is found in text."""
    indices = []
    start = 0
    while True:
        idx = text.find(sub, start)
        if idx == -1:
            break
        indices.append(idx)
        start = idx + 1
    return indices


if __name__ == "__main__":
    text = "abracadabra"
    substring = "abra"
    positions = find_all(text, substring)
    print(f"Text: '{text}'")
    print(f"Substring: '{substring}'")
    print(f"Found at indices: {positions}")
    print(f"Total occurrences: {len(positions)}")
