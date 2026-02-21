"""Groups and capturing in regular expressions."""

import re


def extract_date_parts(date_str):
    """Extract year, month, day using capturing groups."""
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_str)
    if match:
        return {"year": match.group(1), "month": match.group(2), "day": match.group(3)}
    return None


def extract_named_groups(text):
    """Use named groups to extract structured data."""
    pattern = r"(?P<first>\w+)\s(?P<last>\w+),\sage\s(?P<age>\d+)"
    match = re.search(pattern, text)
    return match.groupdict() if match else None


def find_repeated_words(text):
    """Find repeated words using backreferences."""
    return re.findall(r"\b(\w+)\s+\1\b", text, re.IGNORECASE)


if __name__ == "__main__":
    print("Date parts:", extract_date_parts("2026-02-21"))
    print("Named groups:", extract_named_groups("John Doe, age 30"))
    print("Repeated words:", find_repeated_words("The the cat sat sat on a mat"))
    # Non-capturing group example
    results = re.findall(r"(?:Mr|Mrs|Ms)\.\s(\w+)", "Mr. Smith and Mrs. Jones")
    print("Names after title:", results)
