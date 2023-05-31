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
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self._size

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value (int): The size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculate area of the square.
        Returns:
            int: the area of the square
        """
        return self._size ** 2

    def my_print(self):
        """Print the representation of the square in stdout"""
        for i in range(self._size):
            for j in range(self._size):
                print("#", end="")
            print("")
        if self._size == 0:
            print("")
