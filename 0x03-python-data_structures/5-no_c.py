#!/usr/bin/python3

def no_c(my_string):
    remove = ['c', 'C']
    my_string = ''.join(i for i in my_string if not i in remove)
    print(my_string)
