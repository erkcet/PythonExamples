"""Setup and teardown patterns for test fixtures."""

import unittest
import tempfile
import os


class TestWithFixtures(unittest.TestCase):
    """Demonstrate setUp, tearDown, and class-level fixtures."""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests in this class."""
        cls.temp_dir = tempfile.mkdtemp()
        print(f"\nCreated temp dir: {cls.temp_dir}")

    def setUp(self):
        """Run before each test method."""
        self.filepath = os.path.join(self.temp_dir, "test.txt")
        with open(self.filepath, "w") as f:
            f.write("hello")

    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.filepath))

    def test_file_content(self):
        with open(self.filepath) as f:
            self.assertEqual(f.read(), "hello")

    def tearDown(self):
        """Run after each test method."""
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests in this class."""
        os.rmdir(cls.temp_dir)
        print(f"Removed temp dir: {cls.temp_dir}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
