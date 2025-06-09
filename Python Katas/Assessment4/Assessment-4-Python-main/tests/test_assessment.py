import unittest
from assessment import (
    get_list_element_or_default,
    count_value_occurrences,
    create_student_record,
    find_largest_number_in_list,
    combine_string_list
)

class TestCoreAssessmentFunctions(unittest.TestCase):

    def test_get_list_element_or_default(self):
        my_list = [10, 20, 30]
        self.assertEqual(get_list_element_or_default(my_list, 0), 10)
        self.assertEqual(get_list_element_or_default(my_list, 2), 30)
        self.assertIsNone(get_list_element_or_default(my_list, 3)) # Default is None
        self.assertEqual(get_list_element_or_default(my_list, -1, default_value="Not Found"), 30) # Valid negative index
        self.assertEqual(get_list_element_or_default(my_list, -4, default_value="Not Found"), "Not Found") # Invalid negative index
        self.assertEqual(get_list_element_or_default([], 0, default_value="Empty"), "Empty")

    def test_count_value_occurrences(self):
        self.assertEqual(count_value_occurrences([1, 2, 2, 3, 2, 4], 2), 3)
        self.assertEqual(count_value_occurrences([1, 2, 3, 4], 5), 0)
        self.assertEqual(count_value_occurrences([], 1), 0)
        self.assertEqual(count_value_occurrences(["a", "b", "a", "c"], "a"), 2)
        self.assertEqual(count_value_occurrences([True, False, True], True), 2)

    def test_create_student_record(self):
        record1 = create_student_record("Alice Smith", "S123", ["Math101", "CS101"])
        expected1 = {"name": "Alice Smith", "id": "S123", "courses_enrolled": ["Math101", "CS101"]}
        self.assertEqual(record1, expected1)

        record2 = create_student_record("Bob Johnson", 9876, [])
        expected2 = {"name": "Bob Johnson", "id": 9876, "courses_enrolled": []}
        self.assertEqual(record2, expected2)

    def test_find_largest_number_in_list(self):
        self.assertEqual(find_largest_number_in_list([1, 5, 2, 8, 3]), 8)
        self.assertEqual(find_largest_number_in_list([-1, -5, -2, -8, -3]), -1)
        self.assertEqual(find_largest_number_in_list([10]), 10)
        self.assertEqual(find_largest_number_in_list([5, 0, -5, 10]), 10)
        self.assertIsNone(find_largest_number_in_list([]))

    def test_combine_string_list(self):
        self.assertEqual(combine_string_list(["Hello", "World"]), "Hello World")
        self.assertEqual(combine_string_list(["Python", "is", "fun"], joiner_char="-"), "Python-is-fun")
        self.assertEqual(combine_string_list(["OneString"]), "OneString")
        self.assertEqual(combine_string_list([]), "")
        self.assertEqual(combine_string_list(["Test", "with", "custom"], joiner_char="***"), "Test***with***custom")


if __name__ == '__main__':
    unittest.main(verbosity=2)