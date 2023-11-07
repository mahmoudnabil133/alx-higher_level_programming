#!/usr/bin/python3
""" this is my module"""


def read_file(filename=""):
    """ define a function"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
