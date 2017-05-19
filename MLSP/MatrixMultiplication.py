import numpy as np


def product(mat1, mat2):
    result = np.zeros((len(mat1), len(mat2[0])))
    for i in range(len(mat1)):
        # iterate through columns of Y
        for j in range(len(mat2[0])):
            # iterate through rows of Y
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


if __name__ == '__main__':
    mat1 = np.array([[12, 7, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    mat2 = np.array([[5, 8, 1, 2],
                     [6, 7, 3, 0],
                     [4, 5, 9, 1]])

    print product(mat1, mat2)
