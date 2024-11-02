# test_example.py

import unittest
from userA_example_program import format_string as userA_format
from userB_example_program import format_string as userB_format


class TestExampleFunctions(unittest.TestCase):

    def test_userA_format(self):
        self.assertEqual(userA_format("Alice"), "Hello, Alice!")  # This should pass

    def test_userB_format(self):
        self.assertEqual(userB_format("Bob"), "Hello, Bob!")  # This should fail due to intentional mistake


if __name__ == "__main__":
    unittest.main()
