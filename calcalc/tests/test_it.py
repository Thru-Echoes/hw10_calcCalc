from unittest import TestCase
import math
from numpy import inf, isinf, nan, isnan
import adder

class TestOneNumber(TestCase):
    def test_floats(self):
        for num in [1617161771.7650001, math.pi, math.pi**100, math.pi**-100, 3.1]:
            self.assertEqual(calculate(str(num) + '**2', do_float = True), pow(num, 2))

    def test_add_int(self):
        self.assertEqual(calculate('2+2', do_int = True), 4)

    def test_add_float(self):
        self.assertEqual(calculate('2+2', do_float = True), 4.0)

    def test_power(self):
        self.assertTrue(abs(4. - calculate('2**2')) < .001)

    def test_moon(self):
        what_is_moon = 7.345 * (10**22)
        self.assertTrue(calculate('mass of the moon in kg', do_float = True)) >= what_is_moon)
