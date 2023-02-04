#!/usr/bin/python3
"""Task 4"""


def print_square(size):
    """Function that prints a square with the character"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
