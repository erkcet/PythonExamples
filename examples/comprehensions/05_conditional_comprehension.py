"""Comprehensions with if/else conditions."""


def classify_numbers(nums):
    """Classify numbers as positive, negative, or zero."""
    return ["pos" if x > 0 else "neg" if x < 0 else "zero" for x in nums]


def fizzbuzz(n):
    """FizzBuzz using conditional comprehension."""
    return [
        "FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0
        else "Buzz" if i % 5 == 0 else i
        for i in range(1, n + 1)
    ]


def clamp(values, lo, hi):
    """Clamp values to [lo, hi] range."""
    return [max(lo, min(hi, v)) for v in values]


def grade(scores):
    """Convert scores to letter grades."""
    return {
        name: ("A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "F")
        for name, s in scores.items()
    }


if __name__ == "__main__":
    nums = [-3, 0, 5, -1, 2]
    print(f"Classified: {classify_numbers(nums)}")
    print(f"FizzBuzz(15): {fizzbuzz(15)}")
    print(f"Clamped: {clamp([1, 5, 10, 15, 20], 3, 12)}")
    scores = {"Alice": 92, "Bob": 75, "Charlie": 88, "Diana": 65}
    print(f"Grades: {grade(scores)}")
