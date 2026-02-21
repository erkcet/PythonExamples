"""Parse log file entries using regular expressions."""

import re

LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})"
    r"\s+\[(?P<level>\w+)\]\s+"
    r"(?P<message>.+)"
)


def parse_log_line(line):
    """Parse a single log line into components."""
    match = LOG_PATTERN.match(line)
    return match.groupdict() if match else None


def filter_by_level(log_lines, level):
    """Filter log entries by severity level."""
    return [parse_log_line(l) for l in log_lines
            if parse_log_line(l) and parse_log_line(l)["level"] == level]


def extract_error_codes(log_lines):
    """Extract error codes (e.g., E1001) from log messages."""
    codes = []
    for line in log_lines:
        codes.extend(re.findall(r"E\d{4}", line))
    return codes


if __name__ == "__main__":
    logs = [
        "2026-02-21 10:30:00 [INFO] Server started on port 8080",
        "2026-02-21 10:30:05 [ERROR] Connection failed E1001: timeout",
        "2026-02-21 10:31:00 [WARNING] High memory usage detected",
        "2026-02-21 10:32:00 [ERROR] Disk full E2002: no space left",
    ]
    for line in logs:
        print("Parsed:", parse_log_line(line))

    print("\nErrors only:", filter_by_level(logs, "ERROR"))
    print("Error codes:", extract_error_codes(logs))
