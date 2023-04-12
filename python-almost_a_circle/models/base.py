#!/usr/bin/python3
"""Module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"

        if list_objs:
            obj_list = [obj.to_dictionary() for obj in list_objs]
        else:
            obj_list = []
        json_str = cls.to_json_string(obj_list)
        with open(filename, "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dm = cls(1, 1)
        elif cls.__name__ == "Square":
            dm = cls(1)
        else:
            dm = None

        dm.update(**dictionary)
        return dm

    @classmethod
    def load_from_file(cls):
        """Load instances from file and return as a list"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_str = f.read()
                obj_list = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in obj_list]
        except FileNotFoundError:
            return []
