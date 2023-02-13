#!/usr/bin/python3
"""Module"""


class Base:
    """Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Inits the function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
