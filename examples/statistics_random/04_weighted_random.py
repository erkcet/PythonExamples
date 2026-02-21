"""Weighted random selection."""

import random
from collections import Counter


def weighted_choice(items: list, weights: list[float]) -> object:
    """Select a random item based on weights."""
    total = sum(weights)
    r = random.uniform(0, total)
    cumulative = 0
    for item, weight in zip(items, weights):
        cumulative += weight
        if r <= cumulative:
            return item
    return items[-1]


def weighted_sample(items: list, weights: list[float], k: int) -> list:
    """Draw k weighted random selections (with replacement)."""
    return [weighted_choice(items, weights) for _ in range(k)]


def verify_distribution(items: list, weights: list[float], trials: int = 10000) -> dict:
    """Run many trials and compare to expected distribution."""
    total_weight = sum(weights)
    results = Counter(weighted_sample(items, weights, trials))
    return {item: results.get(item, 0) / trials
            for item in items}


if __name__ == "__main__":
    random.seed(42)
    colors = ["red", "blue", "green"]
    weights = [5, 3, 2]
    print("Weights:", dict(zip(colors, weights)))
    dist = verify_distribution(colors, weights)
    for color, freq in dist.items():
        bar = "#" * int(freq * 40)
        print(f"  {color:>5}: {freq:.3f} {bar}")
