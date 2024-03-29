#!/usr/bin/python3
"""say_my_name"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name like: <first name> <last name>"""
    if not first_name or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
