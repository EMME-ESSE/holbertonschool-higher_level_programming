#!/usr/bin/python3
def print_last_digit(number):
    las = abs(number) % 10
    print(f"{las}", end="")
    return las
