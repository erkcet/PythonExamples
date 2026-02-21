"""Generate Permutations Recursively.

Generates all possible orderings of a sequence using backtracking.
n! permutations for n elements.
"""


def permutations(arr: list) -> list:
    """Generate all permutations of arr."""
    result = []
    _permute(arr, 0, len(arr) - 1, result)
    return result


def _permute(arr: list, left: int, right: int, result: list) -> None:
    """Backtracking helper for permutation generation."""
    if left == right:
        result.append(arr[:])
        return
    for i in range(left, right + 1):
        arr[left], arr[i] = arr[i], arr[left]
        _permute(arr, left + 1, right, result)
        arr[left], arr[i] = arr[i], arr[left]  # backtrack


def permutations_string(s: str) -> list:
    """Generate all permutations of a string."""
    chars = list(s)
    perms = permutations(chars)
    return ["".join(p) for p in perms]


if __name__ == "__main__":
    print("Permutations of [1,2,3]:")
    for p in permutations([1, 2, 3]):
        print(f"  {p}")
    print(f"\nPermutations of 'ABC': {permutations_string('ABC')}")
