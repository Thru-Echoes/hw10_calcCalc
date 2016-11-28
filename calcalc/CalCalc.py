#! /usr/bin/env python

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

def calculate(sfoo, return_int = False, return_float = False):

    # Class app id for Wolfram
    app_id = 'UAGAWR-3X6Y8W777Q'
    client = wolframalpha.Client(app_id)

    res = client.query(sfoo)
    res_str = (next(res.results).text)
    res_value = (next(res.results).text).split(' ')[0].encode("ascii", "ignore").decode('ascii')

    try:
        res_float = float(res_value.replace('10^', 'e'))
    except ValueError:
        res_float = float(eval(res_value.replace('10^', 'e')))
    res_int = int(res_float)

    # Determine type of output
    if return_float:
        calc_return = res_float
    elif return_int:
        calc_return = res_int
    else:
        calc_return = res_str
    return calc_return

if __name__ == '__main__':
    cli_args = check_args()
    raw_result = calculate(cli_args[0], return_int = cli_args[1], return_float = cli_args[2])
    print('\n-----------------')
    print('The result is: ', raw_result)
    print('-----------------\n')
