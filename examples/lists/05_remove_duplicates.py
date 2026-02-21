"""Remove duplicates from a list while preserving order."""


def remove_duplicates_set(lst):
    """Remove duplicates using a seen set (O(n))."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def remove_duplicates_dict(lst):
    """Remove duplicates using dict.fromkeys (Python 3.7+)."""
    return list(dict.fromkeys(lst))


def remove_duplicates_index(lst):
    """Remove duplicates keeping last occurrence."""
    seen = {}
    for i, item in enumerate(lst):
        seen[item] = i
    return [item for item, _ in sorted(seen.items(), key=lambda x: x[1])]


if __name__ == "__main__":
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Original:    {data}")
    print(f"Set method:  {remove_duplicates_set(data)}")
    print(f"Dict method: {remove_duplicates_dict(data)}")
    print(f"Keep last:   {remove_duplicates_index(data)}")
