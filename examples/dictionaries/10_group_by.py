"""Group items by a key function."""

from collections import defaultdict


def group_by(items, key_func):
    """Group items by the result of key_func."""
    groups = defaultdict(list)
    for item in items:
        groups[key_func(item)].append(item)
    return dict(groups)


def group_by_first_letter(words):
    """Group words by their first letter."""
    return group_by(words, lambda w: w[0].lower())


def group_by_parity(nums):
    """Group numbers into even and odd."""
    return group_by(nums, lambda n: "even" if n % 2 == 0 else "odd")


def group_records(records, field):
    """Group a list of dicts by a given field."""
    return group_by(records, lambda r: r[field])


if __name__ == "__main__":
    words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
    print(f"By letter: {group_by_first_letter(words)}")
    nums = list(range(1, 11))
    print(f"By parity: {group_by_parity(nums)}")
    people = [
        {"name": "Alice", "dept": "Eng"},
        {"name": "Bob", "dept": "Sales"},
        {"name": "Charlie", "dept": "Eng"},
    ]
    grouped = group_records(people, "dept")
    for dept, members in grouped.items():
        print(f"  {dept}: {[m['name'] for m in members]}")
