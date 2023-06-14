#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str, optional): The name of the file to be read. If not provided, an empty string is used as the default value.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

