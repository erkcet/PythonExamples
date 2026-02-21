"""Compress a string by replacing consecutive repeated characters with counts."""


def compress(s):
    """Compress string: 'aabcccccaaa' -> 'a2b1c5a3'. Return original if shorter."""
    if not s:
        return s
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    result = ''.join(compressed)
    return result if len(result) < len(s) else s


if __name__ == "__main__":
    tests = ["aabcccccaaa", "abcdef", "aaaa", "aabb", ""]
    for t in tests:
        print(f"'{t}' -> '{compress(t)}'")
