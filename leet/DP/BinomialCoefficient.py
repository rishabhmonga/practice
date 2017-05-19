import numpy as np


def binomial_coef(n, k):
    coef = np.zeros((n+1, k+1))
    # coef = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if i == 0 or j == 1:
                coef[i][j] = 1
            else:
                coef[i][j] = coef[i - 1][j - 1] + coef[i - 1][j]
    print coef
    return coef[n][k]


def binomial_coef2(n, k):
    # Declaring an empty array
    C = [0 for _ in range(k + 1)]
    C[0] = 1  # since nC0 is 1

    for i in range(1, n + 1):

        # Compute next row of pascal triangle using
        # the previous row
        j = min(i, k)
        while j > 0:
            C[j] += C[j - 1]
            j -= 1

    return C[k]

if __name__ == '__main__':
    n = 5
    k = 2
    print("Value of Comb[" + str(n) + "][" + str(k) + "] is "
          + str(binomial_coef(n, k)))

    print("Value of Comb[" + str(n) + "][" + str(k) + "] is "
          + str(binomial_coef2(n, k)))
