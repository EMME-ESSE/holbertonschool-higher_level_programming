#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    sortedDict = {i: a_dictionary[i] for i in keys}
    for key, value in sortedDict.items():
        print("{}: {}".format(key, value))
