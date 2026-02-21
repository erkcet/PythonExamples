"""List comprehension patterns."""


def squares(n):
    """Generate squares using list comprehension."""
    return [x ** 2 for x in range(1, n + 1)]


def even_filter(lst):
    """Filter even numbers with a condition."""
    return [x for x in lst if x % 2 == 0]


def flatten(matrix):
    """Flatten a 2D list with nested comprehension."""
    return [val for row in matrix for val in row]


def conditional_transform(lst):
    """Apply different transforms based on condition."""
    return ["even" if x % 2 == 0 else "odd" for x in lst]


def string_processing(words):
    """Process strings: strip, lower, filter blanks."""
    return [w.strip().lower() for w in words if w.strip()]


if __name__ == "__main__":
    print(f"Squares(5): {squares(5)}")
    print(f"Evens: {even_filter(range(1, 11))}")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Flatten: {flatten(matrix)}")
    print(f"Transform: {conditional_transform(range(1, 6))}")
    words = ["  Hello ", "", " WORLD ", "  "]
    print(f"Processed: {string_processing(words)}")
