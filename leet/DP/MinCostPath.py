import numpy as np


def min_cost(cost_matrix, m, n):
    dp_table = np.zeros((len(cost_matrix), len(cost_matrix[0])))
    dp_table[0][0] = cost_matrix[0][0]
    for i in range(1, m + 1):
        dp_table[i][0] = dp_table[i - 1][0] + cost_matrix[i][0]

    for j in range(1, n + 1):
        dp_table[0][j] = dp_table[0][j - 1] + cost_matrix[0][j]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp_table[i][j] = min(dp_table[i - 1][j], dp_table[i][j - 1], dp_table[i - 1][j - 1]) + cost_matrix[i][j]

    print(dp_table)
    return dp_table[m][n]


if __name__ == '__main__':
    print(min_cost([[10, 22, 9, 33, 21, 50, 41, 60],
                    [5, 2, 19, 23, 29, 3, 87, 14],
                    [2, 7, 9, 63, 29, 34, 43, 13]],
                   2, 6))

    print('#*~' * 25)

    print(min_cost([[1, 2, 3],
                    [4, 8, 2],
                    [1, 5, 3]], 2, 2))
