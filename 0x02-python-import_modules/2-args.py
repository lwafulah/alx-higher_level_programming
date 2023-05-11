#!/usr/bin/python3

import sys

arg = sys.argv[1:]
num = len(arg)
print(f"num {number of argument(s)}")
if num == 0:
    print(".")
else:
    print("argument{}:".format("s" if num > 1 else ""))
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
