#!/usr/bin/python3

import sys

def sum_args(args):
    solution = sum(map(int, args))
    return (solution)

if __name__ == '__main__':
    args = sys.argv[1:]
    solution = sum_args(args)
    print(solution)
