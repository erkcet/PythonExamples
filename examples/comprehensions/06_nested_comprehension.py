"""Nested comprehensions for matrix operations."""


def create_matrix(rows, cols, default=0):
    """Create a matrix initialized with a default value."""
    return [[default for _ in range(cols)] for _ in range(rows)]


def identity_matrix(n):
    """Create an n x n identity matrix."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matrix_add(a, b):
    """Add two matrices element-wise."""
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_multiply(a, b):
    """Multiply two matrices."""
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


if __name__ == "__main__":
    print(f"3x3 zeros: {create_matrix(3, 3)}")
    ident = identity_matrix(3)
    print("Identity 3x3:")
    for row in ident:
        print(f"  {row}")
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print(f"Add: {matrix_add(a, b)}")
    print(f"Multiply: {matrix_multiply(a, b)}")
