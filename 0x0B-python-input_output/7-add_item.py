#!/usr/bin/python3
"""Defines a function that adds all arguments to a Python list, and then save them to a file"""

import sys
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be saved as JSON.
        filename (str): The name of the file to save the JSON representation to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, 'r') as file:
        obj = json.load(file)

    return obj

# Get the existing list from the file or create a new list
try:
    existing_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_list = []

# Add the arguments to the list
existing_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(existing_list, 'add_item.json')

