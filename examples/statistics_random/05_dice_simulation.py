"""Dice rolling simulation."""

import random
from collections import Counter


def roll_dice(num_dice: int = 1, sides: int = 6) -> list[int]:
    """Roll num_dice dice, each with the given number of sides."""
    return [random.randint(1, sides) for _ in range(num_dice)]


def simulate_rolls(num_dice: int, sides: int, trials: int) -> Counter:
    """Simulate many rolls and count the frequency of each sum."""
    sums = Counter()
    for _ in range(trials):
        sums[sum(roll_dice(num_dice, sides))] += 1
    return sums


def display_distribution(counts: Counter, trials: int) -> None:
    """Display a text bar chart of roll distribution."""
    for value in sorted(counts):
        freq = counts[value] / trials
        bar = "#" * int(freq * 60)
        print(f"  {value:>3}: {freq:.3f} {bar}")


if __name__ == "__main__":
    random.seed(42)
    print("Single roll (2d6):", roll_dice(2, 6))
    print("\n2d6 distribution (10000 trials):")
    counts = simulate_rolls(2, 6, 10000)
    display_distribution(counts, 10000)
