#!/usr/bin/python3
"""Adds two integers"""


def add_integer(a, b=98):
    """Function that adds two integers."""
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return(a+b)
