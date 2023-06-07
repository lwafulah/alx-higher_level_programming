#!/usr/bin/python3
"""Defines a Rectangle"""

class Rectangle:
    """A class that defines a rectangle: (based on 4-rectangle.py)"""

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle Object

        Attributes:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width.

        Returns:
            int: The width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width.

        Attributes:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height.

        Returns:
            int: The height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height.

        Attributes:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area.

        Returns:
            int: The area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter.

        Returns:
            int: The perimeter.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Get the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """
        Get the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print an exit message when deleting an instance of Rectangle."""
        print("Bye rectangle...")

