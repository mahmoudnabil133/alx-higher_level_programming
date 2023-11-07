#!/usr/bin/python3
"""this is module"""
import json


def save_to_json_file(my_obj, filename):
    """define a function"""
    with open(filename, 'w') as f:
        json.dumps(my_obj, f)
