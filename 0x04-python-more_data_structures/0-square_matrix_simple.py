#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for x in matrix:
        n_matrix.append(list(map(lambda x: x**2, x)))
    return (n_matrix)
