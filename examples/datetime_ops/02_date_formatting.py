"""Date formatting with strftime and parsing with strptime."""

from datetime import datetime


def format_date(dt, fmt):
    """Format a datetime object to string using strftime."""
    return dt.strftime(fmt)


def parse_date(date_str, fmt):
    """Parse a date string into a datetime object using strptime."""
    return datetime.strptime(date_str, fmt)


def common_formats(dt):
    """Show a datetime in several common formats."""
    return {
        "ISO": dt.strftime("%Y-%m-%d"),
        "US": dt.strftime("%m/%d/%Y"),
        "EU": dt.strftime("%d/%m/%Y"),
        "Long": dt.strftime("%B %d, %Y"),
        "With time": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "12-hour": dt.strftime("%I:%M %p"),
        "Day name": dt.strftime("%A"),
    }


if __name__ == "__main__":
    now = datetime.now()
    print("Common formats:")
    for name, formatted in common_formats(now).items():
        print(f"  {name:12s}: {formatted}")

    date_str = "February 21, 2026"
    parsed = parse_date(date_str, "%B %d, %Y")
    print(f"\nParsed '{date_str}' -> {parsed}")
    print(f"Re-formatted: {format_date(parsed, '%Y-%m-%d')}")
