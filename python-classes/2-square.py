#!/usr/bin/python3
"""class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Class square"""
    def __init__(self, size=0):
	if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0"))
