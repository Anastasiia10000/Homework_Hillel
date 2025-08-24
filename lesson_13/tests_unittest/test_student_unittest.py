from lesson_13.homeworks import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.valid_name = "Anastasiia"
        self.valid_surname = "Kalyta"
        self.valid_age = 30
        self.valid_grade = 90
        self.valid_changed_grade = 97.5
        self.student = Student("Anastasiia", "Kalyta", 30, 90)
        print(f"\n🔄 Running test: {self._testMethodName}")

    def tearDown(self):
        self.valid_name = None
        self.valid_surname = None
        self.valid_age = None
        self.valid_grade = None
        self.valid_changed_grade = None
        print(f"\n✅ Test completed: {self._testMethodName}")

    def test_student_attributes(self):
        self.assertIn(self.valid_name, self.student.greet(), msg="Name should be correct")
        self.assertIn(self.valid_surname, self.student.greet(), msg="Surname should be correct")
        self.assertIn(str(self.valid_age), self.student.greet(), msg="Age should be correct")
        self.assertIn(str(self.valid_grade), self.student.greet(), msg="Grade (GPA) should be correct")

    def test_student_greed(self):
        expected_result = f"My full name is {self.valid_name} {self.valid_surname}. I'm {self.valid_age} years old. My GPA is {self.valid_grade}"
        actual_result = self.student.greet()
        self.assertEqual(expected_result, actual_result)
        self.assertIsInstance(actual_result, str, msg="Result should have string type")

    def test_student_changed_grade(self):
        actual_result = self.student.change_grade(self.valid_changed_grade)
        self.assertNotEqual(self.valid_grade, self.student.grade, msg="Grade should have been updated")
        self.assertIn(str(self.valid_changed_grade), actual_result)
        self.assertEqual(f"GPA is changed from {self.valid_grade} to {self.valid_changed_grade}", actual_result)

    def test_student_no_change(self):
        actual_result_no_change = self.student.change_grade(self.valid_grade)
        self.assertEqual("GPA without changes", actual_result_no_change)

if __name__ == '__main__':
    unittest.main()