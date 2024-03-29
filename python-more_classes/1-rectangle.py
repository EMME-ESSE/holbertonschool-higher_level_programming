#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """The rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """width getter"""
    @property
    def width(self):
        return self.__width
    """width setter"""
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    """height getter"""
    @property
    def height(self):
        return self.__height
    """height setter"""
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
