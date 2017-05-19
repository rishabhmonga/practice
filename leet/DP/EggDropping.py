import numpy as np
import sys


def egg_drop(n, k):
    eggfloors = np.zeros((n+1, k+1))
    for i in range(1, n+1):
        eggfloors[i][1] = 1
        eggfloors[i][0] = 0
    print eggfloors
    for j in range(1, k+1):
        eggfloors[1][j] = j

    for i in range(2, n+1):
        for j in range(2, k+1):
            eggfloors[i][j] = sys.maxint
            for x in range(1, j+1):
                result = 1 + max(eggfloors[i-1][x-1], eggfloors[i][j-x])
                if result < eggfloors[i][j]:
                    eggfloors[i][j] = result
    print "\n" + "Result : "
    print eggfloors
    return eggfloors[n][k]

if __name__ == '__main__':
    n = 2
    k = 36
    print "Minimum number of trials in worst case with" + str(n) + "eggs and " + str(k) + " floors is " + str(egg_drop(n, k))