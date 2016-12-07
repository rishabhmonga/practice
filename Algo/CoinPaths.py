def path_count(matrix, m, n, k):
    if m < 0 or n < 0 :
        return 0
    if m == 0 and n == 0:
        return k == matrix[m][n]

    return  matrix


if __name__ == '__main__':
    print()