"""itertools.starmap for applying functions to pre-grouped arguments."""

import itertools


def compute_powers(base_exp_pairs):
    """Compute base**exp for pairs using starmap."""
    return list(itertools.starmap(pow, base_exp_pairs))


def format_records(records):
    """Format name-age pairs into strings using starmap."""
    return list(itertools.starmap(
        lambda name, age: f"{name} (age {age})",
        records
    ))


def parallel_add(list_a, list_b):
    """Element-wise addition of two lists using starmap."""
    return list(itertools.starmap(lambda a, b: a + b, zip(list_a, list_b)))


def multi_arg_apply(func, args_list):
    """Apply a function to multiple argument tuples."""
    return list(itertools.starmap(func, args_list))


if __name__ == "__main__":
    pairs = [(2, 3), (3, 2), (10, 3)]
    print("Powers:", compute_powers(pairs))

    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print("Formatted:", format_records(people))

    a = [1, 2, 3, 4]
    b = [10, 20, 30, 40]
    print("Parallel add:", parallel_add(a, b))

    # starmap vs map comparison
    points = [(1, 2), (3, 4), (5, 6)]
    distances = multi_arg_apply(lambda x, y: (x**2 + y**2)**0.5, points)
    print("Distances from origin:", [round(d, 2) for d in distances])
