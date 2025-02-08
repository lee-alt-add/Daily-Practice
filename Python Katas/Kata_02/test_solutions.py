# test_todo.py

import unittest
from solutions import calculate_average, is_palindrome, flatten_list, word_count, find_common_elements

class TestTodoFunctions(unittest.TestCase):

    def test_calculate_average(self):
        """
        Test the calculate_average function with various inputs.
        """
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4, 5]), 3.0, msg="Test normal list")
        self.assertAlmostEqual(calculate_average([10, 20, 30]), 20.0, msg="Test larger numbers")
        self.assertAlmostEqual(calculate_average([-1, -2, -3, -4, -5]), -3.0, msg="Test negative numbers")
        with self.assertRaises(ZeroDivisionError):
            calculate_average([])  # Test empty list

    def test_is_palindrome(self):
        """
        Test the is_palindrome function with various strings.
        """
        self.assertTrue(is_palindrome("racecar"), "Test palindrome string")
        self.assertTrue(is_palindrome("A man a plan a canal Panama"), "Test palindrome with spaces and case")
        self.assertFalse(is_palindrome("hello"), "Test non-palindrome string")
        self.assertTrue(is_palindrome(""), "Test empty string")

    def test_flatten_list(self):
        """
        Test the flatten_list function with various nested lists.
        """
        self.assertEqual(flatten_list([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5], "Test normal nested list")
        self.assertEqual(flatten_list([[1, [2, 3]], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6], "Test deeply nested list")
        self.assertEqual(flatten_list([]), [], "Test empty list")
        self.assertEqual(flatten_list([[], []]), [], "Test list of empty lists")

    def test_word_count(self):
        """
        Test the word_count function with various texts.
        """
        self.assertEqual(word_count("hello world"), {"hello": 1, "world": 1}, "Test simple text")
        self.assertEqual(word_count("the quick brown fox jumps over the lazy dog"), 
                         {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}, 
                         "Test longer text")
        self.assertEqual(word_count(""), {}, "Test empty string")
        self.assertEqual(word_count("a a a b b c"), {"a": 3, "b": 2, "c": 1}, "Test repeated words")

    def test_find_common_elements(self):
        """
        Test the find_common_elements function with various lists.
        """
        self.assertEqual(find_common_elements([1, 2, 3], [3, 4, 5]), {3}, "Test normal lists")
        self.assertEqual(find_common_elements([1, 2, 3], [4, 5, 6]), set(), "Test no common elements")
        self.assertEqual(find_common_elements([1, 2, 2, 3], [2, 3, 4]), {2, 3}, "Test duplicate elements")
        self.assertEqual(find_common_elements([], [1, 2, 3]), set(), "Test one empty list")


if __name__ == "__main__":
    unittest.main()
