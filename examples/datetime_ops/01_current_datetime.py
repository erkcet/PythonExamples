"""Get current date and time using the datetime module."""

from datetime import datetime, date, time


def get_current_datetime():
    """Return the current date and time."""
    return datetime.now()


def get_current_date():
    """Return today's date only."""
    return date.today()


def get_current_time():
    """Return the current time only."""
    return datetime.now().time()


def get_utc_now():
    """Return the current UTC datetime."""
    return datetime.utcnow()


if __name__ == "__main__":
    print("Current datetime:", get_current_datetime())
    print("Current date:    ", get_current_date())
    print("Current time:    ", get_current_time())
    print("UTC now:         ", get_utc_now())
    print("ISO format:      ", get_current_datetime().isoformat())
    print("Components:")
    now = get_current_datetime()
    print(f"  Year={now.year}, Month={now.month}, Day={now.day}")
    print(f"  Hour={now.hour}, Min={now.minute}, Sec={now.second}")
