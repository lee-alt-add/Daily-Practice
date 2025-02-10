import unittest
from student_grades import add_student, calculate_average, has_passed

class TestStudentGrades(unittest.TestCase):
    def setUp(self):
        self.students = {}

    def test_add_student_valid(self):
        add_student(self.students, "Alice", "S001", [78, 85, 90])
        self.assertIn("S001", self.students)
        self.assertEqual(self.students["S001"]["name"], "Alice")

    def test_add_student_duplicate_id(self):
        add_student(self.students, "Bob", "S002", [70, 80, 90])
        with self.assertRaises(ValueError):
            add_student(self.students, "Charlie", "S002", [65, 75, 85])

    def test_calculate_average(self):
        add_student(self.students, "Alice", "S003", [80, 70, 90])
        self.assertAlmostEqual(calculate_average(self.students, "S003"), 80.0)

    def test_has_passed(self):
        add_student(self.students, "Bob", "S004", [40, 50, 55])
        self.assertTrue(has_passed(self.students, "S004"))

    def test_invalid_grades(self):
        with self.assertRaises(ValueError):
            add_student(self.students, "Dan", "S005", [120, -5, 80])

if __name__ == "__main__":
    unittest.main()
