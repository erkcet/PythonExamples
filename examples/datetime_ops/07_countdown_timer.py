"""Calculate time remaining until a future event."""

from datetime import datetime, timedelta


def time_until(target):
    """Calculate the time remaining until a target datetime."""
    remaining = target - datetime.now()
    if remaining.total_seconds() < 0:
        return None
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}


def format_countdown(target):
    """Return a human-readable countdown string."""
    parts = time_until(target)
    if parts is None:
        return "Event has already passed!"
    return f"{parts['days']}d {parts['hours']}h {parts['minutes']}m {parts['seconds']}s"


def days_until_new_year():
    """Calculate days until next New Year's Day."""
    today = datetime.now()
    new_year = datetime(today.year + 1, 1, 1)
    return (new_year - today).days


if __name__ == "__main__":
    events = {
        "New Year 2027": datetime(2027, 1, 1),
        "Summer 2026": datetime(2026, 6, 21),
        "Past event": datetime(2020, 1, 1),
    }
    for name, target in events.items():
        print(f"  {name}: {format_countdown(target)}")

    print(f"\nDays until New Year: {days_until_new_year()}")
