#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A Square class that defines a square with size

    Attributes:
        _size (int): the size of the square
    """
    def __init__(self, size=0):
        """Creates new instances of square

        Args:
            size (int): The size of the square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
            self._size = size
