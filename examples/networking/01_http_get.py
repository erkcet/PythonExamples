"""Simple HTTP GET request using urllib."""

from urllib.request import urlopen, Request
from urllib.error import URLError


def http_get(url, timeout=10):
    """Perform an HTTP GET request and return the response body."""
    request = Request(url, headers={"User-Agent": "Python-Example/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return response.read().decode("utf-8"), response.status
    except URLError as e:
        return str(e), None


def build_request_with_headers(url, headers=None):
    """Build a Request object with custom headers."""
    default_headers = {"Accept": "text/html", "User-Agent": "Python-Example/1.0"}
    if headers:
        default_headers.update(headers)
    return Request(url, headers=default_headers)


if __name__ == "__main__":
    demo_url = "http://example.com"
    print(f"Fetching {demo_url}...")
    body, status = http_get(demo_url)
    if status:
        print(f"Status: {status}")
        print(f"Body length: {len(body)} chars")
        print(f"First 200 chars:\n{body[:200]}")
    else:
        print(f"Request failed: {body}")
