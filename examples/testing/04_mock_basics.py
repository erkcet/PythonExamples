"""Basic mocking with unittest.mock to isolate units under test."""

import unittest
from unittest.mock import MagicMock, patch


def fetch_user_name(api_client, user_id):
    """Fetch a user name from an API client."""
    response = api_client.get(f"/users/{user_id}")
    return response["name"]


class TestFetchUserName(unittest.TestCase):
    """Demonstrate mocking an external dependency."""

    def test_with_magic_mock(self):
        """Use MagicMock to simulate an API client."""
        mock_client = MagicMock()
        mock_client.get.return_value = {"name": "Alice", "id": 1}
        result = fetch_user_name(mock_client, 1)
        self.assertEqual(result, "Alice")
        mock_client.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_patch_print(self, mock_print):
        """Show patching a builtin."""
        print("hello")
        mock_print.assert_called_once_with("hello")


if __name__ == "__main__":
    unittest.main(verbosity=2)
