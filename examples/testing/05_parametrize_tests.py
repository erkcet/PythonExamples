"""Parameterized test patterns using stdlib unittest."""

import unittest


def is_palindrome(s):
    """Return True if s reads the same forwards and backwards."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


class TestPalindrome(unittest.TestCase):
    """Demonstrate parameterized testing with subTest."""

    def test_true_cases(self):
        cases = ["racecar", "madam", "A Santa at NASA", ""]
        for word in cases:
            with self.subTest(word=word):
                self.assertTrue(is_palindrome(word))

    def test_false_cases(self):
        cases = ["hello", "python", "world"]
        for word in cases:
            with self.subTest(word=word):
                self.assertFalse(is_palindrome(word))


def generate_test(func, input_val, expected):
    """Factory to generate individual test methods."""
    def test_method(self):
        self.assertEqual(func(input_val), expected)
    return test_method


# Dynamically add tests
for i, (inp, exp) in enumerate([("level", True), ("abc", False)]):
    name = f"test_dynamic_{i}_{inp}"
    setattr(TestPalindrome, name, generate_test(is_palindrome, inp, exp))


if __name__ == "__main__":
    unittest.main(verbosity=2)
