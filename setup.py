#!/usr/bin/env python
from __future__ import with_statement

import sys
try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError

VERSION = '0.0.1'
DESCRIPTION = "CalCalc: interface to Wolfram Alpha for math queries"

CLASSIFIERS = filter(None, map(str.strip,
"""
Development Status :: 1 - Unstable
Intended Audience :: Graders
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 3.5
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))

setup(
        name="CalCalc",
        version=VERSION,
        description=DESCRIPTION,
        long_description=DESCRIPTION,
        classifiers=CLASSIFIERS,
        author="Oliver Muellerklein",
        author_email="omuellerklein@berkeley.edu",
        url="http://github.com/Thru-Echoes/hw10_calcCalc",
        license="BSD",
        packages=['calcalc', 'calcalc.tests'],
        platforms=['any'],
        install_requires=['pytest','wolframalpha','argparse'],
        tests_require=['pytest']
)
