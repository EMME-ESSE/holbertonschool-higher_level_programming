#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import hidden_4
    lengt = len(argv)        
    if lengt > 1:
        for i in range(1, lengt):
            if argv[2] != '_':
                print("{}".format(argv[i]))
