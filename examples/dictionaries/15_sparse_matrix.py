"""Sparse matrix representation using dictionaries."""


class SparseMatrix:
    """Memory-efficient matrix storing only non-zero elements."""

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    def set(self, r, c, value):
        """Set value at (r, c). Removes if zero."""
        if value != 0:
            self.data[(r, c)] = value
        else:
            self.data.pop((r, c), None)

    def get(self, r, c):
        """Get value at (r, c), default 0."""
        return self.data.get((r, c), 0)

    def add(self, other):
        """Add two sparse matrices."""
        result = SparseMatrix(self.rows, self.cols)
        all_keys = set(self.data) | set(other.data)
        for key in all_keys:
            result.set(*key, self.data.get(key, 0) + other.data.get(key, 0))
        return result

    def to_dense(self):
        """Convert to a 2D list."""
        return [[self.get(r, c) for c in range(self.cols)] for r in range(self.rows)]

    def nnz(self):
        """Return number of non-zero elements."""
        return len(self.data)


if __name__ == "__main__":
    m = SparseMatrix(3, 3)
    m.set(0, 0, 1); m.set(1, 1, 2); m.set(2, 2, 3)
    print(f"Sparse (nnz={m.nnz()}): {m.data}")
    print("Dense:")
    for row in m.to_dense():
        print(f"  {row}")
    m2 = SparseMatrix(3, 3)
    m2.set(0, 0, 10); m2.set(0, 2, 5)
    result = m.add(m2)
    print(f"Sum dense:")
    for row in result.to_dense():
        print(f"  {row}")
