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
    if not isinstance(a, float):
        raise TypeError("a must be an integer")
    not isinstance(b, float):
        raise TypeError("b must be an integer")

        a = int(a)
        b = int(b)

    return (a + b)
