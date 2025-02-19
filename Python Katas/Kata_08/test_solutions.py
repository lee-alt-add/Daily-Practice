# test_todo.py

import unittest
from todo import remove_duplicates, longest_substring_without_repeating_chars, group_anagrams, is_valid_parentheses, merge_sorted_lists

class TestTodoFunctions(unittest.TestCase):

    def test_remove_duplicates(self):
        """
        Test the remove_duplicates function with various lists.
        """
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5], "Test normal list")
        self.assertEqual(remove_duplicates(["a", "b", "a", "c", "b"]), ["a", "b", "c"], "Test list of strings")
        self.assertEqual(remove_duplicates([]), [], "Test empty list")
        self.assertEqual(remove_duplicates([1]), [1], "Test single element list")

    def test_longest_substring_without_repeating_chars(self):
        """
        Test the longest_substring_without_repeating_chars function with various strings.
        """
        self.assertEqual(longest_substring_without_repeating_chars("abcabcbb"), 3, "Test normal string")
        self.assertEqual(longest_substring_without_repeating_chars("bbbbb"), 1, "Test all same characters")
        self.assertEqual(longest_substring_without_repeating_chars("pwwkew"), 3, "Test mixed characters")
        self.assertEqual(longest_substring_without_repeating_chars(""), 0, "Test empty string")

    def test_group_anagrams(self):
        """
        Test the group_anagrams function with various lists of words.
        """
        self.assertEqual(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), 
                         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]], "Test normal list")
        self.assertEqual(group_anagrams(["listen", "silent", "enlist", "google", "gooegl"]), 
                         [["listen", "silent", "enlist"], ["google", "gooegl"]], "Test larger anagrams")
        self.assertEqual(group_anagrams([]), [], "Test empty list")
        self.assertEqual(group_anagrams(["a"]), [["a"]], "Test single word")

    def test_is_valid_parentheses(self):
        """
        Test the is_valid_parentheses function with various strings of parentheses.
        """
        self.assertTrue(is_valid_parentheses("()"), "Test single pair of parentheses")
        self.assertTrue(is_valid_parentheses("()[]{}"), "Test multiple pairs of parentheses")
        self.assertFalse(is_valid_parentheses("(]"), "Test mismatched parentheses")
        self.assertFalse(is_valid_parentheses("([)]"), "Test nested but invalid parentheses")
        self.assertTrue(is_valid_parentheses("{[]}"), "Test nested valid parentheses")
        self.assertTrue(is_valid_parentheses(""), "Test empty string")

    def test_merge_sorted_lists(self):
        """
        Test the merge_sorted_lists function with various sorted lists.
        """
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6], "Test normal lists")
        self.assertEqual(merge_sorted_lists([], [1, 2, 3]), [1, 2, 3], "Test one empty list")
        self.assertEqual(merge_sorted_lists([1, 2, 3], []), [1, 2, 3], "Test other empty list")
        self.assertEqual(merge_sorted_lists([], []), [], "Test both empty lists")
        self.assertEqual(merge_sorted_lists([1, 4, 7], [2, 5, 8]), [1, 2, 4, 5, 7, 8], "Test no overlapping elements")


if __name__ == "__main__":
    unittest.main()