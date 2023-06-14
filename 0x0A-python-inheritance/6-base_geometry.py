#!/usr/bin/python3
"""Defines a class BaseGeometry (based on 5-base_geometry.py"""

class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: If the area() method is not implemented in the subclass.

        """
        raise Exception("area() is not implemented")

