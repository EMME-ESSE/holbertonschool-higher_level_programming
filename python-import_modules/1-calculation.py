#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, mul, add, div
    a = 10
    b = 5
    addR = add(a, b)
    subR = sub(a, b)
    mulR = mul(a, b)
    divR = div(a, b)
    print("{} + {} = {}".format(a, b, addR))
    print("{} - {} = {}".format(a, b, subR))
    print("{} * {} = {}".format(a, b, mulR))
    print("{} / {} = {}".format(a, b, divR))
