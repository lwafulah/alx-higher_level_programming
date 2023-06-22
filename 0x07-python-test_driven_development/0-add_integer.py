#!/usr/bin/python3
"""Defines an addition function"""

def add_integer(a, b=98):

    """
    Adds two integers.

    Parameters:
        a (int or float): The first integer or float.
        b (int or float): The second integer or float. Default is 98.

    Returns:
        int: The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
