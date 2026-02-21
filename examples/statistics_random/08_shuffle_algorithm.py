"""Fisher-Yates shuffle algorithm."""

import random


def fisher_yates_shuffle(arr: list) -> list:
    """Shuffle a list in-place using Fisher-Yates algorithm."""
    result = arr.copy()
    for i in range(len(result) - 1, 0, -1):
        j = random.randint(0, i)
        result[i], result[j] = result[j], result[i]
    return result


def verify_uniformity(n: int, trials: int = 100000) -> list[list[int]]:
    """Verify shuffle uniformity by counting position frequencies."""
    counts = [[0] * n for _ in range(n)]
    original = list(range(n))
    for _ in range(trials):
        shuffled = fisher_yates_shuffle(original)
        for pos, val in enumerate(shuffled):
            counts[val][pos] += 1
    return counts


if __name__ == "__main__":
    random.seed(42)
    deck = list(range(1, 11))
    print(f"Original: {deck}")
    print(f"Shuffled: {fisher_yates_shuffle(deck)}")
    print(f"Shuffled: {fisher_yates_shuffle(deck)}")

    print("\nUniformity test (4 elements, 100k trials):")
    print("Expected frequency per cell: 25000")
    counts = verify_uniformity(4)
    for val, row in enumerate(counts):
        print(f"  Value {val}: {row}")
