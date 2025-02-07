# test_todo.py

import unittest
from solutions import add_two_numbers, reverse_string, find_largest_number, count_vowels, fibonacci_sequence

class TestTodoFunctions(unittest.TestCase):

    def test_add_two_numbers(self):
        """
        Test the add_two_numbers function with various inputs.
        """
        self.assertEqual(add_two_numbers(5, 7), 12, "Test positive integers")
        self.assertEqual(add_two_numbers(-3, -6), -9, "Test negative integers")
        self.assertEqual(add_two_numbers(-4, 10), 6, "Test mixed positive and negative integers")
        self.assertEqual(add_two_numbers(0, 0), 0, "Test zero values")

    def test_reverse_string(self):
        """
        Test the reverse_string function with various strings.
        """
        self.assertEqual(reverse_string("hello"), "olleh", "Test normal string")
        self.assertEqual(reverse_string("a"), "a", "Test single character string")
        self.assertEqual(reverse_string("racecar"), "racecar", "Test palindrome string")
        self.assertEqual(reverse_string(""), "", "Test empty string")

    # def test_find_largest_number(self):
    #     """
    #     Test the find_largest_number function with various lists of integers.
    #     """
    #     self.assertEqual(find_largest_number([3, 1, 7, 4, 9]), 9, "Test normal list")
    #     self.assertEqual(find_largest_number([5, 5, 5, 5]), 5, "Test all same numbers")
    #     self.assertEqual(find_largest_number([-10, -3, -1, -7]), -1, "Test negative numbers")
    #     self.assertEqual(find_largest_number([0]), 0, "Test single element list")

    def test_count_vowels(self):
        """
        Test the count_vowels function with various strings.
        """
        self.assertEqual(count_vowels("hello"), 2, "Test normal string")
        self.assertEqual(count_vowels("aeiou"), 5, "Test all vowels")
        self.assertEqual(count_vowels("bcdfg"), 0, "Test no vowels")
        self.assertEqual(count_vowels("HELLO"), 2, "Test uppercase vowels")
        self.assertEqual(count_vowels(""), 0, "Test empty string")

    # def test_fibonacci_sequence(self):
    #     """
    #     Test the fibonacci_sequence function with various inputs.
    #     """
    #     self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3], "Test small n")
    #     self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "Test larger n")
    #     self.assertEqual(fibonacci_sequence(1), [0], "Test single element")
    #     self.assertEqual(fibonacci_sequence(0), [], "Test zero input")


if __name__ == "__main__":
    unittest.main()