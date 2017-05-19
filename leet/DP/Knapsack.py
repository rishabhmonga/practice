import numpy as np


def knapsack(weights, values, capcaity):
    benefit = np.zeros((len(values) + 1, capcaity + 1))
    for i in range(1, len(values) + 1):
        for w in range(1, capcaity + 1):
            if weights[i-1] > w:
                benefit[i][w] = benefit[i - 1][w]
            else:
                benefit[i][w] = max(benefit[i - 1][w], values[i-1] + benefit[i - 1][w - weights[i-1]])
    return benefit[len(values)][capcaity]


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapsack(wt, val, W))
