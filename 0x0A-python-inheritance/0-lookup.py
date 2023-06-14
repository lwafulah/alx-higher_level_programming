#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: Object for which to retrieve the attributes and methods.

    Returns:
        A list of the available attributes and methods of the object.
    """
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    return attributes + methods
