#!/usr/bin/python3
"""module load_from_json_file"""


import json


def load_from_json_file(filename):
    """function load_from_json_file"""
    with open(filename, encoding="UTF-8") as fl:
        return json.load(fl)
