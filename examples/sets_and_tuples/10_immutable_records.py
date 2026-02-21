"""Using tuples and namedtuples as immutable records."""

from collections import namedtuple

Employee = namedtuple("Employee", ["name", "dept", "salary"])


def create_records():
    """Create a list of employee records."""
    return [
        Employee("Alice", "Engineering", 95000),
        Employee("Bob", "Marketing", 72000),
        Employee("Charlie", "Engineering", 88000),
        Employee("Diana", "Marketing", 81000),
    ]


def filter_by_dept(records, dept):
    """Filter records by department."""
    return [r for r in records if r.dept == dept]


def average_salary(records):
    """Calculate average salary from records."""
    return sum(r.salary for r in records) / len(records)


def update_record(record, **kwargs):
    """Create a new record with updated fields (immutable update)."""
    return record._replace(**kwargs)


if __name__ == "__main__":
    employees = create_records()
    for emp in employees:
        print(f"  {emp.name}: {emp.dept}, ${emp.salary:,}")
    eng = filter_by_dept(employees, "Engineering")
    print(f"Engineering avg: ${average_salary(eng):,.0f}")
    updated = update_record(employees[0], salary=105000)
    print(f"Updated: {updated}")
    print(f"Original unchanged: {employees[0]}")
