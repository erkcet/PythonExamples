"""Interleave two strings character by character."""


def interleave(s1, s2):
    """Interleave characters from s1 and s2, appending leftovers."""
    result = []
    i = 0
    while i < len(s1) or i < len(s2):
        if i < len(s1):
            result.append(s1[i])
        if i < len(s2):
            result.append(s2[i])
        i += 1
    return ''.join(result)


if __name__ == "__main__":
    pairs = [("abc", "123"), ("hello", "XY"), ("AB", "wxyz")]
    for a, b in pairs:
        print(f"interleave('{a}', '{b}') -> '{interleave(a, b)}'")
