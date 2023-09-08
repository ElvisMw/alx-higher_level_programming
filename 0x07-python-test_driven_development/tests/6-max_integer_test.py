#!/usr/bin/python3
import unittest

# Import the max_integer function from the module '6-max_integer'
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test when the list is ordered."""
        ordered = [2, 4, 6, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test when the list is unordered."""
        unordered = [8, 1, 6, 7]
        self.assertEqual(max_integer(unordered), 8)

    def test_max_at_begginning(self):
        """Test when the maximum value is at the beginning of the list."""
        max_at_beginning = [8, 5, 4, 1]
        self.assertEqual(max_integer(max_at_beginning), 8)

    def test_empty_list(self):
        """Test when the list is empty."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test when the list contains only one element."""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_floats(self):
        """Test when the list contains floating-point numbers."""
        floats = [11.52, 5.21, -5.123, 1.2, 9.0]
        self.assertEqual(max_integer(floats), 11.52)

    def test_ints_and_floats(self):
        """Test when the list contains a mix of integers and floats."""
        ints_and_floats = [14.3, 0.4, -3, 12, 7]
        self.assertEqual(max_integer(ints_and_floats), 14.3)

    def test_string(self):
        """Test when the input is a string."""
        string = "crate"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test when the list contains strings."""
        strings = ["Hot", "tea", "in", "cup"]
        self.assertEqual(max_integer(strings), "cup")

    def test_empty_string(self):
        """Test when an empty string is provided as input."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
