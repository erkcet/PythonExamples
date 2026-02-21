"""Check if one string is a rotation of another."""


def is_rotation(s1, s2):
    """Return True if s2 is a rotation of s1."""
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1


def get_all_rotations(s):
    """Return all rotations of a string."""
    return [s[i:] + s[:i] for i in range(len(s))]


if __name__ == "__main__":
    word = "abcde"
    print(f"All rotations of '{word}':")
    for rot in get_all_rotations(word):
        print(f"  {rot}")
    print(f"Is 'cdeab' a rotation of '{word}'? {is_rotation(word, 'cdeab')}")
    print(f"Is 'abced' a rotation of '{word}'? {is_rotation(word, 'abced')}")
