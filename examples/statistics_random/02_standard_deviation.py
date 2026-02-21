"""Calculate standard deviation and variance."""

import math


def variance(data: list[float], population: bool = True) -> float:
    """Calculate variance (population or sample)."""
    if len(data) < 2:
        raise ValueError("Need at least 2 data points")
    avg = sum(data) / len(data)
    sq_diff = sum((x - avg) ** 2 for x in data)
    return sq_diff / (len(data) if population else len(data) - 1)


def std_dev(data: list[float], population: bool = True) -> float:
    """Calculate standard deviation."""
    return math.sqrt(variance(data, population))


def z_scores(data: list[float]) -> list[float]:
    """Calculate z-scores for each data point."""
    avg = sum(data) / len(data)
    sd = std_dev(data)
    return [(x - avg) / sd for x in data]


if __name__ == "__main__":
    data = [10, 12, 23, 23, 16, 23, 21, 16]
    print(f"Data: {data}")
    print(f"Population variance:  {variance(data):.4f}")
    print(f"Sample variance:      {variance(data, population=False):.4f}")
    print(f"Population std dev:   {std_dev(data):.4f}")
    print(f"Sample std dev:       {std_dev(data, population=False):.4f}")
    print(f"Z-scores: {[f'{z:.2f}' for z in z_scores(data)]}")
