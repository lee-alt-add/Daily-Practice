import unittest
from unittest.mock import patch
import io
from data_structures import *

class TestPerson(unittest.TestCase):
    def test_create_person(self):
        result = create_person("Alice", "Johnson", 30)
        
        self.assertEqual(result["name"], "Alice")
        self.assertEqual(result["surname"], "Johnson")
        self.assertEqual(result["age"], 30)

    def test_update_age(self):
        person = {"name": "Alice", "surname": "Johnson", "age": 30}
        
        update_age(person, 35)
        self.assertEqual(person["age"], 35)

    def test_add_phone_number(self):
        person = {"name": "Alice", "surname": "Johnson", "age": 30}
        
        add_phone_number(person, "123-456-7890")
        self.assertEqual(person["phone_number"], "123-456-7890")

    def test_remove_age(self):
        person = {"name": "Alice", "surname": "Johnson", "age": 30}
        
        remove_age(person)
        self.assertNotIn("age", person)

    def test_display_person_info(self):
        person = {"name": "Alice", "surname": "Johnson", "age": 30}
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            display_person_info(person)
            self.assertEqual(fake_out.getvalue(), "name: Alice\nsurname: Johnson\nage: 30\n")

    def test_get_keys(self):
        person = {"name": "Alice", "surname": "Johnson", "age": 30}
        
        result = get_keys(person)
        self.assertListEqual(result, ["name", "surname", "age"])

    def test_get_values(self):
        person = {"name": "Alice", "surname": "Johnson", "age": 30}
        
        result = get_values(person)
        self.assertListEqual(result, ["Alice", "Johnson", 30])

    def test_create_coordinates(self):
        result = create_coordinates(3, 4)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (3, 4))

    def test_append_to_list(self):
        result = append_to_list([1, 2, 3], 4)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_add_to_set(self):
        result = add_to_set({1, 2, 3}, 4)
        self.assertIsInstance(result, set)
        self.assertIn(4, result)

    def test_process_data(self):
        data = [("Alice", 30), ("Bob", 25), ("Alice", 35)]
        result = process_data(data)
         
        self.assertIsInstance(result, dict)
        self.assertIn("Alice", result)
        self.assertIn("Bob", result)
        self.assertEqual(result["Alice"], {30, 35})
        self.assertEqual(result["Bob"], {25})

    def test_get_element_at_index(self):
        lst = ["apple", "banana", "cherry"]
        
        self.assertEqual(get_element_at_index(lst, 0), "apple")
        self.assertEqual(get_element_at_index(lst, 1), "banana")
        self.assertEqual(get_element_at_index(lst, 2), "cherry")
        
        with self.assertRaises(IndexError):
            get_element_at_index(lst, 3)

    def test_double_values(self):
        result = double_values([1, 2, 3, 4])
        self.assertEqual(result, [2, 4, 6, 8])

    def test_sum_2d_list(self):
        data = [[1, 2, 3], [4, 5], [6]]
        
        self.assertEqual(sum_2d_list(data), 21)
    
    def test_find_max_2d_list(self):
        data = [[1, 2, 3], [4, 5], [6]]
        
        self.assertEqual(find_max_2d_list(data), 6)

    def test_unique_values_from_2d_list(self):
        data = [[1, 2, 3], [2, 4], [3, 5, 6]]

        self.assertEqual(unique_values_from_2d_list(data), [1, 2, 3, 4, 5, 6])
if __name__ == '__main__':
    unittest.main()
