"""Parse and construct URLs using urllib.parse."""

from urllib.parse import urlparse, urlunparse, urlencode, parse_qs, urljoin


def parse_url(url):
    """Parse a URL into its components."""
    parsed = urlparse(url)
    return {
        "scheme": parsed.scheme, "host": parsed.hostname,
        "port": parsed.port, "path": parsed.path,
        "query": parse_qs(parsed.query), "fragment": parsed.fragment,
    }


def build_url(base, path, params=None):
    """Construct a URL from components."""
    url = urljoin(base, path)
    if params:
        url += "?" + urlencode(params)
    return url


def add_query_params(url, params):
    """Add query parameters to an existing URL."""
    separator = "&" if "?" in url else "?"
    return url + separator + urlencode(params)


if __name__ == "__main__":
    test_url = "https://example.com:8080/api/users?page=1&limit=10#results"
    print("Parsed:", parse_url(test_url))
    built = build_url("https://api.example.com", "/v2/search", {"q": "python", "page": "1"})
    print("Built:", built)
    extended = add_query_params(built, {"sort": "date"})
    print("Extended:", extended)
