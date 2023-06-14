#!/usr/bin/python3
"""Defines a class-to-JSON function."""

def class_to_json(obj):
    """
    Returns a dictionary description with a simple data structure suitable for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary representation of the object.
    """
    if not hasattr(obj, '__dict__'):
        return obj

    result = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value

    return result
