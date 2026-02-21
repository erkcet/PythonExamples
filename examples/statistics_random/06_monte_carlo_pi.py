"""Estimate pi using Monte Carlo simulation."""

import random
import math


def estimate_pi(num_points: int) -> float:
    """Estimate pi by random points in a unit square.

    Points falling inside the unit circle quarter give ratio pi/4.
    """
    inside = 0
    for _ in range(num_points):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4.0 * inside / num_points


def convergence_demo(max_points: int) -> list[tuple[int, float]]:
    """Show how the estimate improves with more points."""
    results = []
    n = 100
    while n <= max_points:
        est = estimate_pi(n)
        results.append((n, est))
        n *= 10
    return results


if __name__ == "__main__":
    random.seed(42)
    print("Monte Carlo Pi Estimation")
    print(f"{'Points':>10} {'Estimate':>10} {'Error':>10}")
    print("-" * 32)
    for n, est in convergence_demo(1_000_000):
        error = abs(est - math.pi)
        print(f"{n:>10,} {est:>10.6f} {error:>10.6f}")
    print(f"\n{'actual':>10} {math.pi:>10.6f}")
