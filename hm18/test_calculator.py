import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sum_positiv(self):
        self.assertEqual(self.calculator.sum(1, 5), 6)

    def test_dif_positiv(self):
        self.assertEqual(self.calculator.dif(8, 5), 3)

    def test_mul_positiv(self):
        self.assertEqual(self.calculator.mul(7, 5), 35)

    def test_div_positiv(self):
        self.assertEqual(self.calculator.div(25, 5), 5)

    def test_sum_negativ(self):
        self.assertNotEqual(self.calculator.sum(1, 17), 15)

    def test_dif_negativ(self):
        self.assertNotEqual(self.calculator.dif(13, 5), 4)

    def test_mul_negativ(self):
        self.assertNotEqual(self.calculator.mul(10, 5), 17)

    def test_div_error(self):
        self.assertRaises(ZeroDivisionError, self.calculator.div, 10, 0)


if __name__ == "__main__":
    unittest.main()
