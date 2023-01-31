#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """Public instance for the area"""
        return self.__size ** 2
