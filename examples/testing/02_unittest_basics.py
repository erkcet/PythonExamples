"""Basic unittest example with a small test suite."""

import unittest


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


class TestMultiply(unittest.TestCase):
    """Tests for the multiply function."""

    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_with_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_mixed_sign(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_returns_float_with_float_input(self):
        self.assertIsInstance(multiply(2.0, 3), float)


if __name__ == "__main__":
    unittest.main(verbosity=2)
