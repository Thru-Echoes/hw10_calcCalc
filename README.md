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
    $ python3 setup.py test
```

### Install

```
    $ python3 
    $ python3 setup.py install
```

## Integrate with Flask x Docker

Integration with Flask:

```
    $ python3 app.py
    ...listening on 0.0.0.0:5000
```

Go to the URL **0.0.0.0:5000** in your browser and you will see the result of:

```
    >>> from calcalc.CalCalc import calculate
    >>> calculate('2+2', return_int = True)
```
