"""Zip and unzip operations on lists."""


def zip_lists(*lists):
    """Zip multiple lists into tuples."""
    return list(zip(*lists))


def unzip(pairs):
    """Unzip a list of tuples into separate lists."""
    return [list(x) for x in zip(*pairs)]


def zip_with_fill(*lists, fill=None):
    """Zip with fill value for uneven lists (like zip_longest)."""
    from itertools import zip_longest
    return list(zip_longest(*lists, fillvalue=fill))


def zip_to_dict(keys, values):
    """Create a dictionary from two lists."""
    return dict(zip(keys, values))


if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]
    scores = [95, 87, 92]
    ages = [25, 30, 28]
    print(f"Zipped: {zip_lists(names, scores, ages)}")
    pairs = list(zip(names, scores))
    print(f"Unzipped: {unzip(pairs)}")
    short, long = [1, 2], [10, 20, 30]
    print(f"Zip with fill: {zip_with_fill(short, long, fill=0)}")
    print(f"Zip to dict: {zip_to_dict(names, scores)}")
