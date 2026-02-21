"""Flatten nested lists of arbitrary depth."""

from itertools import chain


def flatten_shallow(nested):
    """Flatten one level using itertools.chain."""
    return list(chain.from_iterable(nested))


def flatten_deep(nested):
    """Recursively flatten lists of any depth."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_deep(item))
        else:
            result.append(item)
    return result


def flatten_generator(nested):
    """Flatten using a generator for memory efficiency."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item


if __name__ == "__main__":
    shallow = [[1, 2], [3, 4], [5, 6]]
    print(f"Shallow flatten: {flatten_shallow(shallow)}")
    deep = [1, [2, [3, [4, [5]]]], [6, 7]]
    print(f"Deep flatten: {flatten_deep(deep)}")
    print(f"Generator flatten: {list(flatten_generator(deep))}")
