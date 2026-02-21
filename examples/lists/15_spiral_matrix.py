"""Spiral matrix traversal."""


def spiral_order(matrix):
    """Return elements of matrix in spiral order."""
    if not matrix:
        return []
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result


def generate_spiral(n):
    """Generate an n x n matrix filled in spiral order."""
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right, num = 0, n - 1, 0, n - 1, 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            matrix[top][c] = num; num += 1
        top += 1
        for r in range(top, bottom + 1):
            matrix[r][right] = num; num += 1
        right -= 1
        for c in range(right, left - 1, -1):
            matrix[bottom][c] = num; num += 1
        bottom -= 1
        for r in range(bottom, top - 1, -1):
            matrix[r][left] = num; num += 1
        left += 1
    return matrix


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Spiral order: {spiral_order(m)}")
    spiral = generate_spiral(4)
    print("Generated 4x4 spiral:")
    for row in spiral:
        print(f"  {row}")
