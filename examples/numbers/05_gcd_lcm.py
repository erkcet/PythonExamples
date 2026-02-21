"""Calculate GCD and LCM."""

import math


def gcd(a: int, b: int) -> int:
    """Calculate Greatest Common Divisor using Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate Least Common Multiple."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def gcd_multiple(*numbers: int) -> int:
    """Calculate GCD of multiple numbers."""
    result = numbers[0]
    for n in numbers[1:]:
        result = gcd(result, n)
    return result


def lcm_multiple(*numbers: int) -> int:
    """Calculate LCM of multiple numbers."""
    result = numbers[0]
    for n in numbers[1:]:
        result = lcm(result, n)
    return result


if __name__ == "__main__":
    pairs = [(12, 18), (35, 14), (100, 75)]
    for a, b in pairs:
        print(f"GCD({a}, {b}) = {gcd(a, b)},  LCM({a}, {b}) = {lcm(a, b)}")
    print(f"\nGCD(12, 18, 24) = {gcd_multiple(12, 18, 24)}")
    print(f"LCM(4, 6, 10) = {lcm_multiple(4, 6, 10)}")
