#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    if idx > len(my_list):
        return(my_list)
    else:
        for i in range(len(my_list)):
            if my_list[idx] in [idx]:
                my_list[idx] = element
