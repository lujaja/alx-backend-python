#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Define class TestAccessNestedMap
    """
    @parameterized.expand([
        ({"a": 1}, ('a'), 1),
        ({"a": {"b": 2}}, ('a'), {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a')),
        ({"a": 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Define TestGetJson
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, test_payload, mock_get):
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = test_payload

        self.assertEqual(get_json(url), test_payload)
        mock_get.assert_called_once_with(url)
        mock_get.reset_mock()


if __name__ == '__main__':
    unittest.main()
