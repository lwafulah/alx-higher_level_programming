#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """A Square class that defines a square with size

    Attributes:
        _size (int): the size of the square
        _position (tuple): the position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square object

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the Square"""
        return self._position

    @position.setter
    def position(self, value):
        """Sets the position of the Square


        Args:
            value (tuple): a tuple of two positive integers

        Raises:
            TypeError: If value is not a tuple of two positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or type(value[0]) != int or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate area of the square.
        Returns:
            int: the area of the square
        """
        return self._size ** 2

    def my_print(self):
        """Prints the representation of the square in stdout"""
        padding = " " * self._position[0]
        for i in range(self._position[1]):
            print("")
        for i in range(self._size):
            print(padding, end="")
            for j in range(self._size):
                print("#", end="")
            print("")
        if self._size == 0:
            print("")
