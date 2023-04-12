#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """Inits the function"""

    if n <= 0:
        return []

    triangle = []
    current_row = [1]
    triangle.append(current_row)

    for j in range(1, n):
        next_row = [1]
        for j in range(1, len(current_row)):
            next_val = current_row[j-1] + current_row[j]
            next_row.append(next_val)
        next_row.append(1)
        triangle.append(next_row)
        current_row = next_row

    return triangle
