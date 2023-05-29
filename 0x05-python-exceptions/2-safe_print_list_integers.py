#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    result = ""
    for i in my_list:
        try:
            result += "{:d}".format(i)
            count += 1
            if count == x:
                break
        except (ValueError, TypeError):
            continue
    print(result.strip())
    return count
