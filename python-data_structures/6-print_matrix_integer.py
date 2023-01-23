#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in (matrix):
        y = 0
        while y <= len(x)-1:
            if y != len(x)-1:
                print('{:d}'.format(x[y]), end=" ")
            else:
                print('{:d}'.format(x[y]), end="")
            y += 1
        print("")
