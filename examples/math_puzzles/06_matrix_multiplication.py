"""Matrix multiplication implementation."""


def matrix_multiply(a, b):
    """Multiply two matrices (lists of lists)."""
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    assert cols_a == rows_b, "Incompatible dimensions"
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(cols_a))
    return result


def identity_matrix(n):
    """Create an n x n identity matrix."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matrix_power(m, p):
    """Raise a square matrix to a power."""
    n = len(m)
    result = identity_matrix(n)
    for _ in range(p):
        result = matrix_multiply(result, m)
    return result


def print_matrix(m, label=""):
    """Pretty-print a matrix."""
    if label:
        print(f"{label}:")
    for row in m:
        print("  [" + ", ".join(f"{x:4d}" for x in row) + "]")


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print_matrix(a, "A")
    print_matrix(b, "B")
    print_matrix(matrix_multiply(a, b), "A * B")
    print_matrix(matrix_power(a, 3), "A^3")
