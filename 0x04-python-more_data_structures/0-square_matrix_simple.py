#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for i in matrix:
        n_matrix.append(list(map(lambda i: i**2, i)))
    return n_matrix
