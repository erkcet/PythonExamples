"""Check and generate magic squares."""


def is_magic_square(matrix):
    """Check if a matrix is a magic square."""
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False
    target = sum(matrix[0])
    rows = all(sum(row) == target for row in matrix)
    cols = all(sum(matrix[r][c] for r in range(n)) == target for c in range(n))
    diag1 = sum(matrix[i][i] for i in range(n)) == target
    diag2 = sum(matrix[i][n - 1 - i] for i in range(n)) == target
    return rows and cols and diag1 and diag2


def generate_odd_magic_square(n):
    """Generate an odd-order magic square using the Siamese method."""
    assert n % 2 == 1, "n must be odd"
    sq = [[0] * n for _ in range(n)]
    r, c = 0, n // 2
    for num in range(1, n * n + 1):
        sq[r][c] = num
        nr, nc = (r - 1) % n, (c + 1) % n
        if sq[nr][nc]:
            nr, nc = (r + 1) % n, c
        r, c = nr, nc
    return sq


def magic_constant(n):
    """Calculate the magic constant for an n x n magic square."""
    return n * (n * n + 1) // 2


if __name__ == "__main__":
    sq = generate_odd_magic_square(5)
    for row in sq:
        print([f"{x:2d}" for x in row])
    print(f"Magic constant: {magic_constant(5)}")
    print(f"Is magic: {is_magic_square(sq)}")
