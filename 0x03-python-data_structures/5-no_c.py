#!/usr/bin/python3

def no_c(my_string):
    char_list = list(my_string)

    for char in ['c', 'C']:
        while char in char_list:
            char_list.remove(char)

    new_string = ''.join(char_list)

    return new_string
