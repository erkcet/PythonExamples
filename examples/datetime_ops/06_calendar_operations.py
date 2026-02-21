"""Calendar module usage for calendar-related operations."""

import calendar


def print_month_calendar(year, month):
    """Return a formatted text calendar for a given month."""
    return calendar.month(year, month)


def is_leap_year(year):
    """Check if a year is a leap year."""
    return calendar.isleap(year)


def get_weekday(year, month, day):
    """Get the day of the week (0=Monday, 6=Sunday)."""
    day_num = calendar.weekday(year, month, day)
    return calendar.day_name[day_num]


def days_in_month(year, month):
    """Get the number of days in a given month."""
    return calendar.monthrange(year, month)[1]


if __name__ == "__main__":
    print(print_month_calendar(2026, 2))
    print(f"2026 is leap year: {is_leap_year(2026)}")
    print(f"2024 is leap year: {is_leap_year(2024)}")
    print(f"2026-02-21 is a: {get_weekday(2026, 2, 21)}")
    print(f"Days in Feb 2026: {days_in_month(2026, 2)}")
    print(f"Days in Feb 2024: {days_in_month(2024, 2)}")

    print(f"\nLeap years 2020-2040: {calendar.leapdays(2020, 2040)}")
