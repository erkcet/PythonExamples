"""itertools.chain and zip_longest for combining iterables."""

import itertools


def flatten_lists(*lists):
    """Flatten multiple lists into one using chain."""
    return list(itertools.chain(*lists))


def flatten_nested(nested):
    """Flatten a list of lists using chain.from_iterable."""
    return list(itertools.chain.from_iterable(nested))


def zip_with_fill(*iterables, fillvalue=None):
    """Zip iterables of unequal length, filling shorter ones."""
    return list(itertools.zip_longest(*iterables, fillvalue=fillvalue))


def interleave(*iterables):
    """Interleave elements from multiple iterables."""
    result = []
    for group in itertools.zip_longest(*iterables):
        result.extend(x for x in group if x is not None)
    return result


if __name__ == "__main__":
    a, b, c = [1, 2], [3, 4, 5], [6]
    print("Chain:", flatten_lists(a, b, c))
    print("Flatten nested:", flatten_nested([[1, 2], [3], [4, 5, 6]]))

    names = ["Alice", "Bob"]
    scores = [90, 85, 78]
    print("\nzip_longest:", zip_with_fill(names, scores, fillvalue="N/A"))
    print("Interleave:", interleave([1, 2, 3], ["a", "b"], ["x"]))

    # chain with different iterable types
    combined = list(itertools.chain("abc", range(3), [True, False]))
    print("Mixed types:", combined)
