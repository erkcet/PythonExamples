"""Parse phone numbers in various formats using regex."""

import re


def parse_phone(phone_str):
    """Parse a US phone number from various formats."""
    pattern = r"(?:\+?1[-.\s]?)?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})"
    match = re.match(pattern, phone_str.strip())
    if match:
        return {"area": match.group(1), "exchange": match.group(2), "number": match.group(3)}
    return None


def normalize_phone(phone_str):
    """Normalize a phone number to (XXX) XXX-XXXX format."""
    parts = parse_phone(phone_str)
    if parts:
        return f"({parts['area']}) {parts['exchange']}-{parts['number']}"
    return None


def find_phones_in_text(text):
    """Find all phone numbers in a block of text."""
    pattern = r"(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)


if __name__ == "__main__":
    formats = ["(555) 123-4567", "555.123.4567", "+1-555-123-4567",
                "5551234567", "1 (555) 123 4567"]
    for phone in formats:
        print(f"  {phone:22s} -> {normalize_phone(phone)}")

    text = "Call 555-100-2000 or (800) 555-1234 for info."
    print("\nFound in text:", find_phones_in_text(text))
