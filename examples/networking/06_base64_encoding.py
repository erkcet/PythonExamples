"""Base64 encoding and decoding operations."""

import base64


def encode_string(text):
    """Encode a string to base64."""
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def decode_string(b64_text):
    """Decode a base64 string back to plaintext."""
    return base64.b64decode(b64_text.encode("ascii")).decode("utf-8")


def encode_urlsafe(text):
    """URL-safe base64 encoding (replaces +/ with -_)."""
    return base64.urlsafe_b64encode(text.encode("utf-8")).decode("ascii")


def encode_bytes(data):
    """Encode raw bytes to base64."""
    return base64.b64encode(data).decode("ascii")


if __name__ == "__main__":
    original = "Hello, Python Base64!"
    encoded = encode_string(original)
    decoded = decode_string(encoded)
    print(f"Original:  {original}")
    print(f"Encoded:   {encoded}")
    print(f"Decoded:   {decoded}")
    print(f"URL-safe:  {encode_urlsafe('data with +/= chars?')}")
    print(f"Bytes:     {encode_bytes(bytes(range(16)))}")
