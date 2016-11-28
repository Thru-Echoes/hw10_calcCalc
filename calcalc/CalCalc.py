#!/usr/bin/env python

""" Calcalc source code: interface with Wolfram Alpha for math queries"""

import wolframalpha
import argparse
from unittest import TestCase
import math

def check_args():
    parser = argparse.ArgumentParser(description = 'CalCalc app: interface with Wolfram Alpha for math queries')
    parser.add_argument('-s', action = 'store', dest = 'math_query',
                        help = 'Store a string value to parse as math query')
    parser.add_argument('-i', action = 'store_true', default = False,
                        dest = 'int_switch',
                        help = 'Set integer output as true')
    parser.add_argument('-f', action = 'store_true', default = False,
                        dest = 'float_switch',
                        help = 'Set float output as true')
    parser.add_argument('--version', action = 'version', version = '%(prog)s 1.0')

    results = parser.parse_args()
    print('\nRequired_args    =', results.math_query)
    print('Int_switch       =', results.int_switch)
    print('Float_switch     =', results.float_switch)
    print('\n')
    return (results.math_query, results.int_switch, results.float_switch)

def calculate(sfoo, do_int = False, do_float = False):

    # Class app id for Wolfram
    app_id = 'UAGAWR-3X6Y8W777Q'
    client = wolframalpha.Client(app_id)

    res = client.query(sfoo)
    res_str = (next(res.results).text)
    res_value = (next(res.results).text).split(' ')[0].encode("ascii", "ignore").decode('ascii')
    res_float = float(res_value.replace('10^', 'e'))
    res_int = int(res_float)

    # Determine type of output
    if do_float:
        calc_return = res_float
    elif do_int:
        calc_return = res_int
    else:
        calc_return = res_str
    return calc_return

def test_add_int():
    assert calculate('2+2', do_int = True) == 4

def test_add_float():
    assert calculate('2+2', do_float = True) == 4.0

def test_power():
    assert abs(4. - calculate('2**2')) < .001

def test_moon():
    what_is_moon = 7.345 * (10**22)
    assert (calculate('mass of the moon in kg', do_float = True)) >= what_is_moon

class TestOneNumber(TestCase):
    def test_floats(self):
        for num in [1617161771.7650001, math.pi, math.pi**100, math.pi**-100, 3.1]:
            self.assertEqual(calculate(str(num) + '**2', do_float = True), pow(num, 2))

if __name__ == '__main__':
    cli_args = check_args()
    raw_result = calculate(cli_args[0], do_int = cli_args[1], do_float = cli_args[2])
    print('\n-----------------')
    print('The result is: ', raw_result)
    print('-----------------\n')
