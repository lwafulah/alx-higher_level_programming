#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square = [[0 for _ in range(len(row))] for row in matrix]
    for i in range(len(matrix)):
        square[i] = list(map(lambda x: x ** 2, matrix[i]))

        return square
