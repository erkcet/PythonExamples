"""Tuple creation, packing, unpacking, and usage."""


def tuple_creation():
    """Various ways to create tuples."""
    empty = ()
    single = (42,)  # note the trailing comma
    packed = 1, 2, 3  # packing without parens
    from_list = tuple([4, 5, 6])
    return empty, single, packed, from_list


def unpacking_examples():
    """Demonstrate tuple unpacking patterns."""
    point = (10, 20, 30)
    x, y, z = point
    first, *rest = (1, 2, 3, 4, 5)
    *init, last = (1, 2, 3, 4, 5)
    a, _, c = (10, 20, 30)  # ignore middle
    return (x, y, z), (first, rest), (init, last), (a, c)


def swap_and_return():
    """Tuples for swapping and multiple return values."""
    a, b = 5, 10
    a, b = b, a  # swap
    return a, b


if __name__ == "__main__":
    for name, t in zip(["empty", "single", "packed", "from_list"], tuple_creation()):
        print(f"{name}: {t} (type={type(t).__name__})")
    coords, (first, rest), (init, last), (a, c) = unpacking_examples()
    print(f"Unpack: x,y,z={coords}, first={first} rest={rest}")
    print(f"Swapped: {swap_and_return()}")
