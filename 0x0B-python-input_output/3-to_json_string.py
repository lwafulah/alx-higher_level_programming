#!/usr/bin/python3
"""Defines an object(string) to JSON function"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    json_string = json.dumps(my_obj)
    return json_string

