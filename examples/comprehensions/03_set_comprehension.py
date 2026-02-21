"""Set comprehensions for unique-element collections."""


def unique_modulos(lst, mod):
    """Get unique results of lst elements modulo mod."""
    return {x % mod for x in lst}


def extract_domains(emails):
    """Extract unique domains from email addresses."""
    return {email.split("@")[1] for email in emails if "@" in email}


def difference_set(a, b):
    """Elements in a but not in b via comprehension."""
    return {x for x in a if x not in b}


def char_frequency_keys(text):
    """Unique characters that appear more than once."""
    from collections import Counter
    counts = Counter(text.lower())
    return {ch for ch, n in counts.items() if n > 1 and ch.isalpha()}


if __name__ == "__main__":
    nums = list(range(20))
    print(f"Unique mod 5: {unique_modulos(nums, 5)}")
    emails = ["a@x.com", "b@y.org", "c@x.com", "d@z.net"]
    print(f"Domains: {extract_domains(emails)}")
    print(f"Diff {{1..5}} - {{3..7}}: {difference_set(range(1,6), range(3,8))}")
    print(f"Repeated chars: {char_frequency_keys('mississippi')}")
