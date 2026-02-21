"""Replace characters in a string using a translation table."""


def replace_chars(s, mapping):
    """Replace characters according to a dict mapping."""
    result = []
    for ch in s:
        result.append(mapping.get(ch, ch))
    return ''.join(result)


def leet_speak(s):
    """Convert a string to simple leet speak."""
    table = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    return replace_chars(s.lower(), table)


if __name__ == "__main__":
    text = "Hello World"
    print(f"Original:  {text}")
    print(f"Leet:      {leet_speak(text)}")
    custom = replace_chars(text, {'l': 'L', 'o': '0'})
    print(f"Custom:    {custom}")
