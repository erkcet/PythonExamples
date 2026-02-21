"""Generate all permutations of a string."""


def permutations(s):
    """Return all permutations of the string as a sorted list."""
    if len(s) <= 1:
        return [s]
    result = []
    for i, ch in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for perm in permutations(remaining):
            result.append(ch + perm)
    return sorted(set(result))


if __name__ == "__main__":
    tests = ["abc", "ab", "aab"]
    for t in tests:
        perms = permutations(t)
        print(f"Permutations of '{t}' ({len(perms)} total):")
        print(f"  {perms}")
        print()
