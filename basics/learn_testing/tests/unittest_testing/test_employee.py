import unittest
from unittest import TestCase
from employee import Employee

class TestEmployee(TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Class")

    @classmethod
    def tearDownClass(cls):
        print("Tear Down Class")

    def setUp(self):
        print("Setup:")
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print("Tear down!")

    def test_fullname(self):
        print("test_fullname:")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

    def test_email(self):
        print("test_email:")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

if __name__ == '__main__':
    unittest.main()