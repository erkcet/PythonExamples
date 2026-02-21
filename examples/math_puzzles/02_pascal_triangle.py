"""Pascal's triangle generation and properties."""


def pascal_triangle(n):
    """Generate the first n rows of Pascal's triangle."""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1]
        triangle.append(row)
    return triangle


def pascal_row(n):
    """Get the nth row (0-indexed) of Pascal's triangle."""
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row


def print_triangle(n):
    """Pretty-print Pascal's triangle."""
    triangle = pascal_triangle(n)
    width = len(" ".join(str(x) for x in triangle[-1]))
    for row in triangle:
        line = " ".join(str(x) for x in row)
        print(line.center(width))


if __name__ == "__main__":
    print("Pascal's Triangle (7 rows):")
    print_triangle(7)
    print(f"\nRow 10: {pascal_row(10)}")
    print(f"Sum of row 10: {sum(pascal_row(10))} (= 2^10 = {2**10})")
