#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        value = int(value)  # Convert the value to an integer
        print(value)
        return True
    except ValueError:
        print("Exception: Invalid integer value", file=sys.stderr)
        return False
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
