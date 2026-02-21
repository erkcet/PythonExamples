"""Flatten nested structures using comprehensions."""


def flatten_2d(matrix):
    """Flatten a 2D list into a 1D list."""
    return [val for row in matrix for val in row]


def flatten_dict_values(d):
    """Collect all values from a dict of lists into one list."""
    return [item for values in d.values() for item in values]


def flatten_strings(sentences):
    """Split sentences into a flat list of words."""
    return [word for sentence in sentences for word in sentence.split()]


def flatten_with_filter(matrix, predicate):
    """Flatten and filter simultaneously."""
    return [val for row in matrix for val in row if predicate(val)]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Flat 2D: {flatten_2d(matrix)}")
    groups = {"fruits": ["apple", "banana"], "vegs": ["carrot", "pea"]}
    print(f"Dict values: {flatten_dict_values(groups)}")
    sentences = ["hello world", "foo bar baz"]
    print(f"Words: {flatten_strings(sentences)}")
    print(f"Flat evens: {flatten_with_filter(matrix, lambda x: x % 2 == 0)}")
