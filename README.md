<img src="https://travis-ci.org/Thru-Echoes/hw10_calcCalc.svg?branch=master" data-pin-nopin="true">

# Homework 10 - CalcCalc CLI tool

A Command Line tool written in Python that interfaces with Wolfram Alpha. This is for *homework 10* for the seminar **Python Computing for Data Science**.

```
    $ python calcalc/CalCalc.py -s '2+2' -f
```

### Use as module

```
    >>> from calcalc.CalCalc import calculate
    >>> calculate('2+2', return_int = True)
```

### Run tests

```
    $ python setup.py test
```

### Install

```
    $ python setup.py install
```

## Integrate with Flask x Docker

Coming soon...
