"""Calculate business days (excluding weekends)."""

from datetime import date, timedelta


def is_business_day(d):
    """Check if a date is a business day (Mon-Fri)."""
    return d.weekday() < 5


def add_business_days(start, num_days):
    """Add a number of business days to a date."""
    current = start
    added = 0
    while added < num_days:
        current += timedelta(days=1)
        if is_business_day(current):
            added += 1
    return current


def count_business_days(start, end):
    """Count business days between two dates (exclusive of end)."""
    count = 0
    current = start
    while current < end:
        if is_business_day(current):
            count += 1
        current += timedelta(days=1)
    return count


def next_business_day(d):
    """Find the next business day on or after the given date."""
    while not is_business_day(d):
        d += timedelta(days=1)
    return d


if __name__ == "__main__":
    today = date.today()
    print(f"Today ({today}) is a business day: {is_business_day(today)}")
    print(f"+10 business days: {add_business_days(today, 10)}")

    start = date(2026, 2, 1)
    end = date(2026, 2, 28)
    print(f"\nBusiness days in Feb 2026: {count_business_days(start, end)}")
    print(f"Next business day from Saturday 2026-02-28: {next_business_day(date(2026, 2, 28))}")
