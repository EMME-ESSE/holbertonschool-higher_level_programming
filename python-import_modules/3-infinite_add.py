#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    res = 0
    if length == 1:
        print("{}".format(0))
    elif length > 1:
        for i in range(1, length):
            res += int(argv[i])
        print("{}".format(res))
