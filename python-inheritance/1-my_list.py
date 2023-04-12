#!/usr/bin/python3
"""class list that inherits"""


class MyList(list):
    """Class My list"""
    def print_sorted(self):
        print(sorted(self))
