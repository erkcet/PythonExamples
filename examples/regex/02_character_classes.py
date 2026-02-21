"""Character classes and quantifiers in regular expressions."""

import re


def find_with_classes(text):
    """Demonstrate various character classes."""
    return {
        "digits": re.findall(r"\d+", text),
        "words": re.findall(r"\w+", text),
        "whitespace": re.findall(r"\s+", text),
        "vowels": re.findall(r"[aeiouAEIOU]", text),
        "non_digits": re.findall(r"\D+", text),
    }


def find_with_quantifiers(text):
    """Demonstrate quantifiers: *, +, ?, {n,m}."""
    return {
        "one_or_more_digits": re.findall(r"\d+", text),
        "zero_or_more_a": re.findall(r"a*", text),
        "optional_s": re.findall(r"colou?r", text),
        "exactly_3_digits": re.findall(r"\d{3}", text),
        "2_to_4_digits": re.findall(r"\d{2,4}", text),
    }


if __name__ == "__main__":
    sample = "Hello World 123! The colour/color code is #FF00AB."
    print("Character classes:")
    for key, val in find_with_classes(sample).items():
        print(f"  {key}: {val}")

    print("\nQuantifiers:")
    for key, val in find_with_quantifiers(sample).items():
        print(f"  {key}: {val}")
