"""Tower of Hanoi.

Moves n disks from source to destination using an auxiliary peg.
Requires 2^n - 1 moves. Classic recursion example.
"""


def hanoi(n: int, source: str = "A", target: str = "C", auxiliary: str = "B") -> list:
    """Solve Tower of Hanoi and return list of moves."""
    moves = []
    _hanoi_helper(n, source, target, auxiliary, moves)
    return moves


def _hanoi_helper(n, source, target, auxiliary, moves):
    """Recursive helper for Tower of Hanoi."""
    if n == 1:
        moves.append((source, target))
        return
    _hanoi_helper(n - 1, source, auxiliary, target, moves)
    moves.append((source, target))
    _hanoi_helper(n - 1, auxiliary, target, source, moves)


if __name__ == "__main__":
    for disks in range(1, 5):
        moves = hanoi(disks)
        print(f"\n{disks} disk(s): {len(moves)} moves")
        for src, dst in moves:
            print(f"  Move disk from {src} to {dst}")
