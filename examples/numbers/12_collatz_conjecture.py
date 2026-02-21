"""Collatz sequence (3n+1 problem)."""


def collatz_sequence(n: int) -> list[int]:
    """Generate the Collatz sequence starting from n."""
    if n < 1:
        raise ValueError("Starting number must be positive")
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def collatz_length(n: int) -> int:
    """Return the number of steps to reach 1."""
    return len(collatz_sequence(n)) - 1


def longest_collatz(limit: int) -> tuple[int, int]:
    """Find the starting number under limit with the longest sequence."""
    best_start, best_len = 1, 0
    for i in range(1, limit):
        length = collatz_length(i)
        if length > best_len:
            best_start, best_len = i, length
    return best_start, best_len


if __name__ == "__main__":
    for start in [6, 11, 27]:
        seq = collatz_sequence(start)
        print(f"{start:>3}: {len(seq)-1} steps, max={max(seq)}")
        print(f"     {seq[:10]}{'...' if len(seq) > 10 else ''}")
    num, steps = longest_collatz(1000)
    print(f"\nLongest under 1000: {num} with {steps} steps")
