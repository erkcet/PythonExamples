"""Matrix determinant calculation."""


def determinant(matrix):
    """Calculate the determinant of a square matrix using cofactor expansion."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for col in range(n):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return det


def minor_matrix(matrix, row, col):
    """Get the minor matrix by removing a row and column."""
    return [r[:col] + r[col + 1:] for i, r in enumerate(matrix) if i != row]


def cofactor_matrix(matrix):
    """Compute the cofactor matrix."""
    n = len(matrix)
    return [[(-1) ** (i + j) * determinant(minor_matrix(matrix, i, j))
             for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    m2 = [[3, 8], [4, 6]]
    print(f"2x2 det: {determinant(m2)}")
    m3 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    print(f"3x3 det: {determinant(m3)}")
    m4 = [[1, 2, 3, 4], [5, 6, 7, 8], [2, 6, 4, 8], [3, 1, 1, 2]]
    print(f"4x4 det: {determinant(m4)}")
    print(f"Cofactors of 2x2: {cofactor_matrix(m2)}")
