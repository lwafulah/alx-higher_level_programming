#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    val = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > val:
            val = my_list[i]
    return val
