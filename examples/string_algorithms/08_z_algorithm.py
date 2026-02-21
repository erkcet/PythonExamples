"""Z-algorithm for pattern matching."""


def z_array(s):
    """Compute the Z-array for a string."""
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def z_search(text, pattern):
    """Find all occurrences of pattern in text using Z-algorithm."""
    combined = pattern + "$" + text
    z = z_array(combined)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] == m]


def count_occurrences(text, pattern):
    """Count non-overlapping occurrences using Z-algorithm."""
    return len(z_search(text, pattern))


if __name__ == "__main__":
    text = "aabxaabxcaabxaabxay"
    pattern = "aabx"
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    print(f"Z-array of pattern: {z_array(pattern)}")
    print(f"Found at indices:   {z_search(text, pattern)}")
    print(f"Count: {count_occurrences(text, pattern)}")
    print(f"\nZ-array of 'aabaaab': {z_array('aabaaab')}")
