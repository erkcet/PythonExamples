"""Implement run-length encoding and decoding for strings."""

def encode(s):
    """Compress using run-length encoding."""
    if not s:
        return ""
    result, count = [], 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i-1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return ''.join(result)

def decode(s):
    """Decompress a run-length encoded string."""
    result, i = [], 0
    while i < len(s):
        ch, i, num = s[i], i + 1, ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        result.append(ch * int(num))
    return ''.join(result)

if __name__ == "__main__":
    original = "aaabbbccddddee"
    encoded = encode(original)
    decoded = decode(encoded)
    print(f"Original: {original}")
    print(f"Encoded:  {encoded}")
    print(f"Decoded:  {decoded}")
    print(f"Match:    {original == decoded}")
