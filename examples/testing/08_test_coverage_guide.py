"""Guide to test coverage concepts (demonstration, not real coverage)."""


def calculate_grade(score):
    """Convert a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def demonstrate_coverage_concepts():
    """Show which inputs exercise which code branches."""
    branches = {
        "A (>=90)": [90, 95, 100],
        "B (>=80)": [80, 85],
        "C (>=70)": [70, 75],
        "D (>=60)": [60, 65],
        "F (<60)":  [0, 50, 59],
    }
    print("Branch coverage demonstration for calculate_grade():\n")
    for branch, scores in branches.items():
        results = [(s, calculate_grade(s)) for s in scores]
        print(f"  {branch}: {results}")

    print("\nTo measure real coverage, run:")
    print("  pip install coverage")
    print("  coverage run -m unittest discover")
    print("  coverage report -m")


if __name__ == "__main__":
    demonstrate_coverage_concepts()
