#!/usr/bin/python3

class Square:
    """A class that defines the properties and methods of a square."""

    def __init__(self):
        """Constructor of the class that initializes the side_length of the square to None."""
        self.__side_length = None

    def get_side_length(self):
        """Returns the side_length of the square."""
        return self.__side_length

    def set_side_length(self, side_length):
        """Sets the side_length of the square."""
        self.__side_length = side_length

    pass
