"""Unix timestamp conversions."""

import time
from datetime import datetime, timezone


def datetime_to_timestamp(dt):
    """Convert a datetime object to a Unix timestamp."""
    return dt.timestamp()


def timestamp_to_datetime(ts):
    """Convert a Unix timestamp to a datetime object."""
    return datetime.fromtimestamp(ts)


def timestamp_to_utc(ts):
    """Convert a Unix timestamp to a UTC datetime."""
    return datetime.fromtimestamp(ts, tz=timezone.utc)


def current_timestamp():
    """Get the current Unix timestamp."""
    return time.time()


def iso_to_timestamp(iso_str):
    """Convert an ISO format string to a Unix timestamp."""
    dt = datetime.fromisoformat(iso_str)
    return dt.timestamp()


if __name__ == "__main__":
    now_ts = current_timestamp()
    print(f"Current timestamp: {now_ts}")
    print(f"As local datetime: {timestamp_to_datetime(now_ts)}")
    print(f"As UTC datetime:   {timestamp_to_utc(now_ts)}")

    dt = datetime(2026, 2, 21, 12, 0, 0)
    ts = datetime_to_timestamp(dt)
    print(f"\n{dt} -> timestamp: {ts}")
    print(f"Roundtrip:         {timestamp_to_datetime(ts)}")

    print(f"\nISO to timestamp:  {iso_to_timestamp('2026-02-21T12:00:00')}")
    print(f"Epoch (0):         {timestamp_to_datetime(0)}")
