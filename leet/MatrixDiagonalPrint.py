import numpy as np


def is_valid(i, j, row, col):
    if i < 0 or i >= row or j < 0 or j >= col:
        return False
    return True


def diagonalOrder(matrix, row, col):
    for k in range(row):
        print int(matrix[k][0]),
        i = k - 1
        j = 1

        while is_valid(i, j, row, col):
            print int(matrix[i][j]),
            i -= 1
            j += 1
        print

    for k in range(1, col):
        print int(matrix[row - 1][k]),
        i = row - 2
        j = k + 1

        while is_valid(i, j, row, col):
            print int(matrix[i][j]),
            i -= 1
            j += 1
        print


if __name__ == '__main__':
    matrix = np.zeros((4, 5))
    count = 1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = count
            count += 1

    print matrix
    diagonalOrder(matrix, len(matrix), len(matrix[0]))
