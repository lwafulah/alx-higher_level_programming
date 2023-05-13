#!/usr/bin/python3

import sys

def main(args):
    num = len(args)
    print(f"{num} argument{'s' if num != 1 else ''}:")
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main(sys.argv[1:])
