"""Product, permutations, and combinations from itertools."""

import itertools


def cartesian_product(*iterables):
    """Compute cartesian product of input iterables."""
    return list(itertools.product(*iterables))


def all_permutations(items, r=None):
    """Generate all permutations of a given length."""
    return list(itertools.permutations(items, r))


def all_combinations(items, r):
    """Generate combinations of length r (no repetition)."""
    return list(itertools.combinations(items, r))


def combinations_with_rep(items, r):
    """Generate combinations allowing repeated elements."""
    return list(itertools.combinations_with_replacement(items, r))


if __name__ == "__main__":
    print("Product [1,2] x [a,b]:", cartesian_product([1, 2], ["a", "b"]))
    print("Dice rolls (2d2):", cartesian_product(range(1, 3), repeat=2))

    print("\nPermutations of ABC:")
    for p in all_permutations("ABC"):
        print(f"  {''.join(p)}")

    print("\nCombinations of ABCD choose 2:", all_combinations("ABCD", 2))
    print("With replacement AB choose 2:", combinations_with_rep("AB", 2))
