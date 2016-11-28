from unittest import TestCase
import math
from numpy import inf, isinf, nan, isnan
from calcalc.CalCalc import calculate

class TestOneNumber(TestCase):
    def test_floats(self):
        for num in range(10):
            self.assertEqual(calculate(str(num) + '**2', return_float = True), pow(num, 2))

    def test_add_int(self):
        self.assertEqual(calculate('2+2', return_int = True), 4)

    def test_add_float(self):
        self.assertEqual(calculate('2+2', return_int = False, return_float = True), 4.0)

    def test_pi(self):
        what_is_pi = "%.4f" % math.pi
        self.assertEqual(calculate('pi to 5 digits', return_float = True), eval(what_is_pi))

    def test_moon(self):
        what_is_moon = 7.345 * (10**22)
        self.assertTrue(calculate('mass of the moon in kg', return_float = True) >= what_is_moon)
