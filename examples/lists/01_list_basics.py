"""List basics: creation, access, and modification."""


def demonstrate_creation():
    """Show different ways to create lists."""
    empty = []
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    from_range = list(range(5))
    repeated = [0] * 5
    return empty, numbers, mixed, from_range, repeated


def demonstrate_access(lst):
    """Show indexing and membership testing."""
    first, last = lst[0], lst[-1]
    exists = 3 in lst
    idx = lst.index(3) if 3 in lst else -1
    return first, last, exists, idx


def demonstrate_modification(lst):
    """Show common list mutations."""
    lst.append(6)
    lst.insert(0, 0)
    lst.remove(3)
    popped = lst.pop()
    lst.extend([7, 8])
    lst.sort()
    return lst, popped


if __name__ == "__main__":
    for name, val in zip(["empty", "nums", "mixed", "range", "repeated"], demonstrate_creation()):
        print(f"{name}: {val}")
    nums = [1, 2, 3, 4, 5]
    print(f"Access: first={demonstrate_access(nums)[0]}, last={demonstrate_access(nums)[1]}")
    result, popped = demonstrate_modification(nums.copy())
    print(f"Modified: {result}, popped={popped}")
