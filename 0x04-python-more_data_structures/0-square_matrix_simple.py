#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat2 = matrix.copy()
    x = 0
    for i in matrix:
        y = 0
        for j in i:
            mat2[x][y] == j ** 2
            y += 1
        x += 1
    return (mat2)   
