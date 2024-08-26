#!/usr/bin/env python3
"""Unittest for access_nested_map function
"""
from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ test class
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access nested map
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
