#!/usr/bin/python3
"""
Define a function that rotates an nxn 2D matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2d square matrix
    """
    m = len(matrix)
    for i in range(m):
        for j in range(i):
            temporary = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temporary

    for i in range(m):
        for j in range(int(m / 2)):
            temporary = matrix[i][j]
            matrix[i][j] = matrix[i][m-1-j]
            matrix[i][m-1-j] = temporary
