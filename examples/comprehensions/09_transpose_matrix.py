"""Transpose a matrix using comprehensions and zip."""


def transpose_comprehension(matrix):
    """Transpose using nested list comprehension."""
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def transpose_zip(matrix):
    """Transpose using zip (most Pythonic)."""
    return [list(row) for row in zip(*matrix)]


def transpose_map(matrix):
    """Transpose using map and zip."""
    return list(map(list, zip(*matrix)))


def print_matrix(name, matrix):
    """Pretty-print a matrix."""
    print(f"{name}:")
    for row in matrix:
        print(f"  {row}")


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    print_matrix("Original (2x3)", m)
    print_matrix("Comprehension", transpose_comprehension(m))
    print_matrix("Zip", transpose_zip(m))
    print_matrix("Map", transpose_map(m))
    rect = [[1, 2], [3, 4], [5, 6]]
    print_matrix("Original (3x2)", rect)
    print_matrix("Transposed (2x3)", transpose_zip(rect))
