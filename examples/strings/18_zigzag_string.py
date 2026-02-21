"""Convert a string into a zigzag pattern across a given number of rows."""


def zigzag_convert(s, num_rows):
    """Rearrange string characters in a zigzag pattern and read row by row."""
    if num_rows <= 1 or num_rows >= len(s):
        return s
    rows = [[] for _ in range(num_rows)]
    row, step = 0, 1
    for ch in s:
        rows[row].append(ch)
        if row == 0:
            step = 1
        elif row == num_rows - 1:
            step = -1
        row += step
    return ''.join(''.join(r) for r in rows)


if __name__ == "__main__":
    text = "PAYPALISHIRING"
    for n in range(1, 5):
        result = zigzag_convert(text, n)
        print(f"rows={n}: '{result}'")
