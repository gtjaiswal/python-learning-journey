import unittest
from unittest import TestCase
import calculator

class TestCalculator(TestCase):

    # def setUp(self):
    #     self.calc = calculator.Calculator()

    def test_add(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.add(2,2) ,4)
        self.assertEqual(calc.add(2, 0) , 2)
        self.assertEqual(calc.add(-2, -2) , -4)
        self.assertEqual(calc.add(2, -2) , 0)
        self.assertEqual(calc.add(0, 0) , 0)

    # def test_divide(self):
    #     assert False
    #
    # def test_is_even(self):
    #     assert False

if __name__== '__main__':
    unittest.main()