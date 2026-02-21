"""Date arithmetic: adding and subtracting days, hours, etc."""

from datetime import datetime, timedelta


def add_days(dt, days):
    """Add a number of days to a datetime."""
    return dt + timedelta(days=days)


def subtract_hours(dt, hours):
    """Subtract hours from a datetime."""
    return dt - timedelta(hours=hours)


def days_between(dt1, dt2):
    """Calculate the number of days between two dates."""
    return abs((dt2 - dt1).days)


def add_duration(dt, weeks=0, days=0, hours=0, minutes=0):
    """Add a flexible duration to a datetime."""
    return dt + timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes)


if __name__ == "__main__":
    now = datetime.now()
    print("Now:           ", now)
    print("+30 days:      ", add_days(now, 30))
    print("-5 hours:      ", subtract_hours(now, 5))

    start = datetime(2026, 1, 1)
    end = datetime(2026, 12, 31)
    print(f"\nDays in 2026:  {days_between(start, end)}")

    print("+2w 3d 5h:    ", add_duration(now, weeks=2, days=3, hours=5))

    delta = end - start
    print(f"Timedelta:     {delta} ({delta.total_seconds()} seconds)")
