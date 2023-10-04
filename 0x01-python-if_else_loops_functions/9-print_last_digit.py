#!/usr/bin/python3
def print_last_digit(number):
    dig = abs(number) % 10
    print(f"{dig}", end="")
    return dig
