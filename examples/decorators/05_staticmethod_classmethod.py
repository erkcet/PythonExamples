"""@staticmethod and @classmethod usage and differences."""


class Date:
    """Simple date class demonstrating static and class methods."""

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        """Alternate constructor: create Date from 'YYYY-MM-DD' string."""
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)

    @classmethod
    def today_fixed(cls):
        """Alternate constructor: return a fixed demo date."""
        return cls(2026, 1, 1)

    @staticmethod
    def is_leap_year(year):
        """Check if a year is a leap year (no instance needed)."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"


if __name__ == "__main__":
    d1 = Date.from_string("2024-03-15")
    print(f"From string: {d1}")
    d2 = Date.today_fixed()
    print(f"Fixed today: {d2}")
    print(f"2024 leap? {Date.is_leap_year(2024)}")
    print(f"2023 leap? {Date.is_leap_year(2023)}")
