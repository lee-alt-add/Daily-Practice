import unittest
from patterns import *
class TestLoopsAndShapes(unittest.TestCase):
    

    def test_count_items(self):
        self.assertEqual(count_items([1, 2, 3, 4, 5]), 5)
        self.assertEqual(count_items([]), 0)
        self.assertEqual(count_items(['a', 'b', 'c']), 3)

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_numbers([]), 0)
        self.assertEqual(sum_numbers([-1, 0, 1]), 0)

    def test_find_largest(self):
        self.assertEqual(find_largest([1, 5, 3, 9, 2]), 9)
        self.assertEqual(find_largest([-5, -2, -10]), -2)
        self.assertEqual(find_largest([0]), 0)

    # Easy Tests
    def test_count_even_numbers(self):
        self.assertEqual(count_even_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(count_even_numbers([1, 3, 5, 7, 9]), 0)
        self.assertEqual(count_even_numbers([2, 4, 6, 8]), 4)

    def test_sum_digits(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(9999), 36)
        self.assertEqual(sum_digits(1000000), 1)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_multiply_list_elements(self):
        self.assertEqual(multiply_list_elements([1, 2, 3, 4]), 24)
        self.assertEqual(multiply_list_elements([2, 2, 2]), 8)
        self.assertEqual(multiply_list_elements([1, 0, 5]), 0)

  
    def test_create_number_triangle1(self):
        self.assertEqual(create_number_triangle(3), ['1', '22', '333'])
        self.assertEqual(create_number_triangle(5), ['1', '22', '333', '4444', '55555'])
        self.assertEqual(create_number_triangle(1), ['1'])

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fibonacci_sequence(2), [0, 1])

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("hello world"), "hll wrld")
        self.assertEqual(remove_vowels("AEIOU"), "")
        self.assertEqual(remove_vowels("rhythm"), "rhythm")

    def test_create_multiplication_table(self):
        expected = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
        self.assertEqual(create_multiplication_table(3), expected)

    def test_count_character_frequency(self):
        self.assertEqual(count_character_frequency("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertEqual(count_character_frequency("aabbcc"), {'a': 2, 'b': 2, 'c': 2})

    def test_reverse_words(self):
        self.assertEqual(reverse_words("hello world"), "olleh dlrow")
        self.assertEqual(reverse_words("Python is awesome"), "nohtyP si emosewa")

    
    def test_spiral_matrix(self):
        expected = [[1, 2, 3], 
                    [8, 9, 4], 
                    [7, 6, 5]]
        self.assertEqual(spiral_matrix(3), expected)

    def test_pascal_triangle(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(pascal_triangle(5), expected)

    def test_longest_common_subsequence(self):
        self.assertEqual(longest_common_subsequence("ABCDGH", "AEDFHR"), 3)
        self.assertEqual(longest_common_subsequence("AGGTAB", "GXTXAYB"), 4)

    def test_count_inversions(self):
        self.assertEqual(count_inversions([1, 20, 6, 4, 5]), 5)
        self.assertEqual(count_inversions([1, 2, 3, 4, 5]), 0)

   
    def test_create_hollow_square(self):
        expected = ['***', '* *', '***']
        self.assertEqual(create_hollow_square(3), expected)

    def test_create_diamond(self):
        expected = [' * ', '***', ' * ']
        self.assertEqual(create_diamond(3), expected)

    def test_create_hourglass(self):
        expected = ['*****', ' *** ', '  *  ', ' *** ', '*****']
        self.assertEqual(create_hourglass(5), expected)

    def test_create_spiral_string(self):
        expected = "123\n894\n765"
        self.assertEqual(create_spiral_string(3), expected)

    def test_create_alphabet_diamond(self):
        expected = ['  A  ', ' B B ', 'C   C', ' B B ', '  A  ']
        self.assertEqual(create_alphabet_diamond(3), expected)

    def test_create_number_spiral(self):
        expected = ['123', '894', '765']
        self.assertEqual(create_number_spiral(3), expected)

    def test_create_pyramid(self):
        expected = ['  *  ', ' *** ', '*****']
        self.assertEqual(create_pyramid(3), expected)
        expected = ['   *   ', '  ***  ', ' ***** ', '*******']
        self.assertEqual(create_pyramid(4), expected)

    def test_create_number_triangle(self):
        expected = ['1', '22', '333']
        self.assertEqual(create_number_triangle(3), expected)
        expected = ['1', '22', '333', '4444']
        self.assertEqual(create_number_triangle(4), expected)

if __name__ == '__main__':
    unittest.main()