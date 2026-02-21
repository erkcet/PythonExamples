"""Working with timezones using stdlib only (datetime.timezone)."""

from datetime import datetime, timezone, timedelta


def get_utc_now():
    """Get the current time in UTC with timezone info."""
    return datetime.now(timezone.utc)


def to_timezone(dt, offset_hours):
    """Convert a timezone-aware datetime to another timezone."""
    tz = timezone(timedelta(hours=offset_hours))
    return dt.astimezone(tz)


def create_timezone(name, offset_hours):
    """Create a fixed-offset timezone."""
    return timezone(timedelta(hours=offset_hours), name=name)


if __name__ == "__main__":
    utc_now = get_utc_now()
    print("UTC now:      ", utc_now)

    zones = {"EST": -5, "CST": -6, "PST": -8, "JST": 9, "IST": 5.5}
    for name, offset in zones.items():
        tz = create_timezone(name, offset)
        local_time = utc_now.astimezone(tz)
        print(f"  {name} (UTC{offset:+}): {local_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

    # Naive vs aware comparison
    naive = datetime.now()
    aware = datetime.now(timezone.utc)
    print(f"\nNaive tzinfo: {naive.tzinfo}")
    print(f"Aware tzinfo: {aware.tzinfo}")
