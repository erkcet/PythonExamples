"""Parse and validate URLs using regular expressions."""

import re

URL_PATTERN = re.compile(
    r"^(?P<scheme>https?|ftp)://"
    r"(?P<host>[a-zA-Z0-9.-]+)"
    r"(?::(?P<port>\d+))?"
    r"(?P<path>/[^\s?#]*)?"
    r"(?:\?(?P<query>[^\s#]*))?"
    r"(?:#(?P<fragment>\S*))?$"
)


def parse_url(url):
    """Parse a URL into its components."""
    match = URL_PATTERN.match(url)
    return match.groupdict() if match else None


def is_valid_url(url):
    """Check if a string is a valid HTTP/HTTPS/FTP URL."""
    return bool(URL_PATTERN.match(url))


def extract_urls(text):
    """Extract all URLs from a block of text."""
    return re.findall(r"https?://[^\s<>\"']+", text)


if __name__ == "__main__":
    urls = [
        "https://example.com:8080/path/page?q=hello#section",
        "http://sub.domain.org/api/v1",
        "ftp://files.example.com/pub",
        "not-a-url",
    ]
    for url in urls:
        print(f"  {url}")
        print(f"    valid: {is_valid_url(url)}, parts: {parse_url(url)}\n")

    text = "Visit https://example.com or http://test.org/page for details."
    print("Extracted:", extract_urls(text))
