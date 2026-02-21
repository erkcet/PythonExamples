"""Advanced list slicing techniques."""


def basic_slices(lst):
    """Demonstrate basic slicing with start, stop, step."""
    return {
        "first_three": lst[:3],
        "last_three": lst[-3:],
        "every_other": lst[::2],
        "reversed": lst[::-1],
        "middle": lst[2:5],
    }


def slice_assignment(lst):
    """Replace a slice of a list in place."""
    result = lst.copy()
    result[1:4] = [20, 30, 40]
    return result


def rotate_via_slice(lst, k):
    """Rotate a list using slicing."""
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


def chunk_via_slice(lst, size):
    """Split list into chunks using slicing."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]


if __name__ == "__main__":
    nums = list(range(1, 11))
    print(f"Original: {nums}")
    for name, val in basic_slices(nums).items():
        print(f"  {name}: {val}")
    print(f"Slice assign [1:4]=[20,30,40]: {slice_assignment(nums)}")
    print(f"Rotate by 3: {rotate_via_slice(nums, 3)}")
    print(f"Chunks of 3: {chunk_via_slice(nums, 3)}")
