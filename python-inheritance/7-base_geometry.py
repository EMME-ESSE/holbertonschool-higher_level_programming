#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry:
    """class BaseGeometry"""
    
    def area(self):
        """Raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if int"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
