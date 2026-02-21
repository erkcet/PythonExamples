"""Testing that functions raise the expected exceptions."""

import unittest


def divide(a, b):
    """Divide a by b, raising ValueError on zero division."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def parse_age(value):
    """Parse a string to age, raising TypeError or ValueError."""
    if not isinstance(value, str):
        raise TypeError("Expected a string")
    age = int(value)
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


class TestExceptions(unittest.TestCase):
    """Show different ways to assert exception behavior."""

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_by_zero_message(self):
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0)
        self.assertIn("zero", str(ctx.exception))

    def test_parse_age_type_error(self):
        with self.assertRaises(TypeError):
            parse_age(123)

    def test_parse_age_negative(self):
        with self.assertRaises(ValueError):
            parse_age("-5")

    def test_parse_age_valid(self):
        self.assertEqual(parse_age("25"), 25)


if __name__ == "__main__":
    unittest.main(verbosity=2)
