#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        y = 0
        for j in i:
            y += 1
            if y != len(i):
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print()
