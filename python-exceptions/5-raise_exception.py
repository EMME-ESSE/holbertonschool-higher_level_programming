#!/usr/bin/python3
def raise_exception():
    raise TypeError("This is a custom exception")

    try:
        raise_exception()
    except TypeError as e:
        print(e) 
