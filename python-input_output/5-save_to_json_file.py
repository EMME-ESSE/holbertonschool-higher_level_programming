#!/usr/bin/python3
"""module save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """function save_to_json_file"""
    import json
    with open(filename, 'w') as fl:
        fl.write(json.dumps(my_obj))
