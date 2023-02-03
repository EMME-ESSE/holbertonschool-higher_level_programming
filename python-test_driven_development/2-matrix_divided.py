#!/usr/bin/python3
"""Divides a given matrix by a given number"""


def matrix_divided(matrix, div):
    """division"""
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list or \
    not all(map(lambda x: type(x) == list, matrix)):
        raise TypeError(err)
    if not all(map(lambda x: len(x) == len(matrix[0]), matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(map(lambda x: all\
        (map(lambda y: type(y) in [int, float], x)), matrix)):
        raise TypeError(err)

    return [[round(y / div, 2) for y in x] for x in matrix]