"""Matrix Chain Multiplication.

Determines the most efficient way to multiply a chain of matrices.
Minimizes total scalar multiplications. O(n^3) time.
"""


def matrix_chain_order(dims: list) -> int:
    """Return minimum multiplications for matrices with given dimensions.

    dims[i-1] x dims[i] gives the dimensions of the ith matrix.
    """
    n = len(dims) - 1  # number of matrices
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]


def matrix_chain_parenthesization(dims: list) -> str:
    """Return optimal parenthesization as a string."""
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    def build(i, j):
        if i == j:
            return f"M{i+1}"
        return f"({build(i, split[i][j])} x {build(split[i][j]+1, j)})"
    return build(0, n - 1)


if __name__ == "__main__":
    dimensions = [10, 30, 5, 60]
    print(f"Dimensions: {dimensions}")
    print(f"Min multiplications: {matrix_chain_order(dimensions)}")
    print(f"Optimal order: {matrix_chain_parenthesization(dimensions)}")
