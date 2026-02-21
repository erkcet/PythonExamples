"""Parse and work with HTTP headers (conceptual demo)."""

from email.message import EmailMessage
from http.client import HTTPResponse
from io import BytesIO


def parse_raw_headers(raw):
    """Parse raw HTTP header string into a dictionary."""
    msg = EmailMessage()
    for line in raw.strip().split("\n"):
        if ": " in line:
            key, value = line.split(": ", 1)
            msg[key] = value.strip()
    return dict(msg.items())


def build_headers(**kwargs):
    """Build a headers dictionary with common defaults."""
    defaults = {"Accept": "application/json", "User-Agent": "Python/1.0"}
    defaults.update(kwargs)
    return defaults


def get_content_type(headers):
    """Extract and parse content type from headers."""
    ct = headers.get("Content-Type", "text/plain")
    parts = ct.split(";")
    mime = parts[0].strip()
    params = dict(p.strip().split("=", 1) for p in parts[1:] if "=" in p)
    return mime, params


if __name__ == "__main__":
    raw = "Content-Type: application/json; charset=utf-8\nX-Request-Id: abc123\nCache-Control: no-cache"
    parsed = parse_raw_headers(raw)
    print("Parsed headers:", parsed)
    print("Built headers:", build_headers(Authorization="Bearer token123"))
    mime, params = get_content_type(parsed)
    print(f"MIME: {mime}, Params: {params}")
