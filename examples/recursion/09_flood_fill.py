"""Flood Fill Algorithm.

Recursively fills connected regions with a new color, similar to
the paint bucket tool. Works on a 2D grid.
"""


def flood_fill(image: list, sr: int, sc: int, new_color: int) -> list:
    """Fill connected region starting at (sr, sc) with new_color."""
    image = [row[:] for row in image]  # deep copy
    old_color = image[sr][sc]
    if old_color == new_color:
        return image
    _fill(image, sr, sc, old_color, new_color)
    return image


def _fill(image, r, c, old_color, new_color):
    """Recursive helper for flood fill."""
    if (r < 0 or r >= len(image) or c < 0 or c >= len(image[0])
            or image[r][c] != old_color):
        return
    image[r][c] = new_color
    _fill(image, r + 1, c, old_color, new_color)
    _fill(image, r - 1, c, old_color, new_color)
    _fill(image, r, c + 1, old_color, new_color)
    _fill(image, r, c - 1, old_color, new_color)


def print_grid(grid: list) -> None:
    """Display a 2D grid."""
    for row in grid:
        print("  " + " ".join(str(x) for x in row))


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 0, 2, 2],
        [0, 0, 2, 2, 2],
    ]
    print("Before:")
    print_grid(grid)
    result = flood_fill(grid, 1, 1, 3)
    print("After fill (1,1) with 3:")
    print_grid(result)
