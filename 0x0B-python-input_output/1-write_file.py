#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the count of characters written.

    Parameters:
        filename (str): The name of the file to write to. If not provided, an empty string is used as the default value.
        text (str): The string to be written to the file. If not provided, an empty string is used as the default value.

    Returns:
        int: The count of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        chars = file.write(text)

    return chars
