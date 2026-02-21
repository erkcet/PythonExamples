"""N-Queens Problem.

Places N queens on an NxN chessboard so that no two queens
threaten each other. Uses recursive backtracking.
"""


def solve_n_queens(n: int) -> list:
    """Return all solutions for the N-Queens problem."""
    solutions = []
    _place_queen(n, [], solutions)
    return solutions


def _place_queen(n, queens, solutions):
    """Try placing a queen in each column of the current row."""
    row = len(queens)
    if row == n:
        solutions.append(queens[:])
        return
    for col in range(n):
        if _is_safe(queens, row, col):
            queens.append(col)
            _place_queen(n, queens, solutions)
            queens.pop()


def _is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r, c in enumerate(queens):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def print_board(queens):
    """Display a solution as a chessboard."""
    n = len(queens)
    for r in range(n):
        row = ["Q" if c == queens[r] else "." for c in range(n)]
        print("  " + " ".join(row))


if __name__ == "__main__":
    for n in [4, 8]:
        sols = solve_n_queens(n)
        print(f"\n{n}-Queens: {len(sols)} solutions")
        if sols:
            print("First solution:")
            print_board(sols[0])
