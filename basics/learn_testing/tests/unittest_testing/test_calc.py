import unittest
from unittest import TestCase
from basic import calc


class TestCalc(TestCase):

    def test_add(self):
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(0, 0), 0)

    def test_divide(self):
            self.assertEqual(calc.divide(-1, -1), 1)
            # self.assertEqual(calc.divide(10, 0), 15)
            # self.assertEqual(calc.add(-1, 1), 0)
            # self.assertEqual(calc.add(0, 0), 0)
            self.assertRaises(ValueError, calc.divide, 10, 0)


if __name__== '__main__':
    unittest.main()

