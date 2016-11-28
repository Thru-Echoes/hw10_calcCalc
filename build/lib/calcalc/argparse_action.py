# Code from http://www.doughellmann.com/PyMOTW/argparse/

import argparse
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
print('required_args    =', results.required_string_1, results.required_string_2)
print('simple_value     =', results.simple_value)
print('constant_value   =', results.constant_value)
print('boolean_switch   =', results.boolean_switch)
print('collection       =', results.collection)
print('const_collection =', results.const_collection)
