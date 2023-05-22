#!/usr/bin/python3
def print_alphabet():
    print(''.join(chr(i) for i in range(ord('a'), ord('z') + 1)), end='')
