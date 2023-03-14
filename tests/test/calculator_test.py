from unittest import TestCase, main
from tests.calculator import calculator


class CalculatorTests(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('18-7'), 11)

    def test_multi(self):
        self.assertEqual(calculator('3*9'), 27)

    def test_divide(self):
        self.assertEqual(calculator('74/2'), 37.0)


if __name__ == '__main__':
    main()
