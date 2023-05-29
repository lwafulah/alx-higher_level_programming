#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)  # Call the function with the given arguments
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
