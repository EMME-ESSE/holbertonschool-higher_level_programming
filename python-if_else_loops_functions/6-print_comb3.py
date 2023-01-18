#!/usr/bin/python3
for x in range(9):
    for n in range(x + 1, 10):
        if x == 8 and n == 9:
            print("{:d}{:d}".format(x, n))
        else:
            print("{:d}{:d}".format(x, n), end=', ')
