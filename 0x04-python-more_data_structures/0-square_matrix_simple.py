#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat2 = matrix.copy()
    for i in range(len(matrix)):
        mat2[i] = list(map(lambda x: x ** 2, matrix[i]))
    return (mat2)
