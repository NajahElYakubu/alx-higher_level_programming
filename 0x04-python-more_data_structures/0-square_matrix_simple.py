#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
	n_matrix = matrix
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			n_matrix[i][j] = matrix[i][j] ** 2
	return n_matrix  
