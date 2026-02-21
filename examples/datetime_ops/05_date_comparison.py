"""Compare dates and determine ordering."""

from datetime import datetime, date


def is_future(dt):
    """Check if a date is in the future."""
    return dt > datetime.now() if isinstance(dt, datetime) else dt > date.today()


def is_between(dt, start, end):
    """Check if a date falls between start and end (inclusive)."""
    return start <= dt <= end


def sort_dates(dates):
    """Sort a list of date objects chronologically."""
    return sorted(dates)


def earliest_and_latest(dates):
    """Find the earliest and latest dates from a list."""
    return {"earliest": min(dates), "latest": max(dates)}


if __name__ == "__main__":
    today = date.today()
    past = date(2020, 6, 15)
    future = date(2030, 1, 1)

    print(f"{past} is in the future: {is_future(past)}")
    print(f"{future} is in the future: {is_future(future)}")
    print(f"{today} is between {past} and {future}: {is_between(today, past, future)}")

    dates = [date(2025, 3, 1), date(2023, 12, 25), date(2026, 7, 4), date(2024, 1, 1)]
    print("\nSorted:", sort_dates(dates))
    print("Extremes:", earliest_and_latest(dates))
