"""Mask a credit card number, showing only the last four digits."""


def mask_card(number):
    """Mask all but the last four digits of a credit card number."""
    digits = ''.join(ch for ch in number if ch.isdigit())
    if len(digits) < 4:
        return number
    masked = '*' * (len(digits) - 4) + digits[-4:]
    # Reformat with dashes every 4 characters
    return '-'.join(masked[i:i+4] for i in range(0, len(masked), 4))


if __name__ == "__main__":
    cards = [
        "4111-1111-1111-1111",
        "5500 0000 0000 0004",
        "3782 822463 10005",
        "1234567890123456",
    ]
    for card in cards:
        print(f"{card:30s} -> {mask_card(card)}")
