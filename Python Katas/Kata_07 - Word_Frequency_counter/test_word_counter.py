import unittest
from word_counter import count_word_frequencies

class TestWordCounter(unittest.TestCase):
    def test_count_word_frequencies(self):
        text = "Hello world! Hello everyone."
        expected_output = {"hello": 2, "world": 1, "everyone": 1}
        self.assertEqual(count_word_frequencies(text), expected_output)

    def test_case_insensitivity(self):
        text = "Python python PYTHON"
        expected_output = {"python": 3}
        self.assertEqual(count_word_frequencies(text), expected_output)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            count_word_frequencies("")

    def test_punctuation_removal(self):
        text = "Hello, world! It's a great, great world."
        expected_output = {"hello": 1, "world": 2, "it's": 1, "a": 1, "great": 2}
        self.assertEqual(count_word_frequencies(text), expected_output)

if __name__ == "__main__":
    unittest.main()
