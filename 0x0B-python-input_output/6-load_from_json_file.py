#!/usr/bin/python3
"""this is module"""
import json


def load_from_json_file(filename):
    """define a function"""
    with open(filename, 'r') as f:
        return json.loads(f)
