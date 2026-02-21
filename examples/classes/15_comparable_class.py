"""Making classes sortable and comparable with total_ordering."""

from functools import total_ordering


@total_ordering
class Student:
    """Student comparable by GPA, then by name."""

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (self.gpa, self.name) == (other.gpa, other.name)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (self.gpa, self.name) < (other.gpa, other.name)

    def __repr__(self):
        return f"Student({self.name!r}, gpa={self.gpa})"

    def __hash__(self):
        return hash((self.name, self.gpa))


if __name__ == "__main__":
    students = [
        Student("Charlie", 3.5),
        Student("Alice", 3.9),
        Student("Bob", 3.5),
        Student("Diana", 4.0),
    ]

    print("Sorted:")
    for s in sorted(students):
        print(f"  {s}")

    a, b = Student("Alice", 3.9), Student("Bob", 3.5)
    print(f"\n{a} > {b}: {a > b}")
    print(f"{a} >= {b}: {a >= b}")
    print(f"Max: {max(students)}")
