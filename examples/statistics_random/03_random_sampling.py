"""Random sampling techniques."""

import random


def simple_random_sample(population: list, k: int) -> list:
    """Draw k items from population without replacement."""
    return random.sample(population, k)


def systematic_sample(population: list, k: int) -> list:
    """Select every kth element after a random start."""
    start = random.randint(0, k - 1)
    return [population[i] for i in range(start, len(population), k)]


def stratified_sample(strata: dict[str, list], fraction: float) -> dict[str, list]:
    """Sample a fraction from each stratum."""
    result = {}
    for name, group in strata.items():
        n = max(1, int(len(group) * fraction))
        result[name] = random.sample(group, n)
    return result


def reservoir_sample(stream, k: int) -> list:
    """Reservoir sampling for streams of unknown length."""
    reservoir = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir


if __name__ == "__main__":
    random.seed(42)
    pop = list(range(1, 51))
    print(f"Simple random (5): {simple_random_sample(pop, 5)}")
    print(f"Systematic (k=10): {systematic_sample(pop, 10)}")
    strata = {"A": list(range(1, 21)), "B": list(range(21, 51))}
    print(f"Stratified (20%):  {stratified_sample(strata, 0.2)}")
    print(f"Reservoir (5):     {reservoir_sample(range(100), 5)}")
