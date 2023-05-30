#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A Square class that defines a square with size
    
    Attributes:
        _size (int): the size of the square 
    """
    
    def __init__(self, size=0):
        """Initialize a Square object

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
    
    def area(self):
        """Calculate area of the square.
        Returns:
            int: the area of the square
        """
        return self._size ** 2
