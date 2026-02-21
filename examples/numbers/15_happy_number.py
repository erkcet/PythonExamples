"""Check if a number is happy."""


def sum_of_squares(n: int) -> int:
    """Return the sum of squares of digits of n."""
    return sum(int(d) ** 2 for d in str(n))


def is_happy(n: int) -> bool:
    """Return True if n is a happy number.

    A happy number eventually reaches 1 when replaced by the
    sum of the squares of its digits repeatedly.
    """
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
    return n == 1


def happy_sequence(n: int) -> list[int]:
    """Return the sequence of sums until reaching 1 or a cycle."""
    seq, seen = [n], set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
        seq.append(n)
    return seq


def find_happy_numbers(limit: int) -> list[int]:
    """Find all happy numbers up to limit."""
    return [n for n in range(1, limit + 1) if is_happy(n)]


if __name__ == "__main__":
    for num in [7, 19, 4, 89]:
        seq = happy_sequence(num)
        label = "happy" if is_happy(num) else "sad"
        print(f"{num:>3} ({label:>5}): {seq}")
    print(f"\nHappy numbers 1-100: {find_happy_numbers(100)}")
