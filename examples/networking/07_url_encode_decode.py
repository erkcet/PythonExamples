"""URL encoding and decoding operations."""

from urllib.parse import quote, unquote, urlencode, parse_qs, quote_plus


def encode_path(path):
    """URL-encode a path component (spaces become %20)."""
    return quote(path, safe="/")


def encode_query_value(value):
    """URL-encode a query value (spaces become +)."""
    return quote_plus(value)


def decode_url(encoded):
    """Decode a URL-encoded string."""
    return unquote(encoded)


def build_query_string(params):
    """Build a query string from a dictionary."""
    return urlencode(params)


def parse_query_string(qs):
    """Parse a query string into a dictionary."""
    return parse_qs(qs)


if __name__ == "__main__":
    path = "/api/search results/café"
    print(f"Encoded path: {encode_path(path)}")
    print(f"Encoded query: {encode_query_value('hello world & more')}")
    print(f"Decoded: {decode_url('hello%20world%20%26%20more')}")
    params = {"q": "python tutorial", "lang": "en", "page": "1"}
    qs = build_query_string(params)
    print(f"Query string: {qs}")
    print(f"Parsed back: {parse_query_string(qs)}")
