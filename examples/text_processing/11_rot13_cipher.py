"""Implement the ROT13 cipher for encoding and decoding text."""


def rot13(text):
    """Apply ROT13 substitution cipher. Applying twice returns original."""
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(ch)
    return ''.join(result)


if __name__ == "__main__":
    messages = ["Hello, World!", "Python 3.12", "The Quick Brown Fox"]
    for msg in messages:
        encoded = rot13(msg)
        decoded = rot13(encoded)
        print(f"Original: {msg}")
        print(f"ROT13:    {encoded}")
        print(f"Double:   {decoded}")
        print()
