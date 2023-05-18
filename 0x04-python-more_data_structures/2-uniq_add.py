#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_integers = []

    for item in my_list:
        if type(item) == int and item not in unique_integers:
            unique_integers.append(item)

    total_sum = sum(unique_integers)

    return total_sum
