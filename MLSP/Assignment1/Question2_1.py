import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

import EigenValue


def covariance(X):
    X -= X.mean(axis=0)
    N = X.shape[1]

    fact = float(N - 1)

    return np.dot(X, X.T.conj()) / fact


if __name__ == '__main__':
    X = loadmat("./X.mat")
    A = X['X']
    B = np.dot(A, A.T)
    print B.shape
    l1, v1 = EigenValue.eigen(B)
    l2, v2 = EigenValue.eigen(B - l1 * np.dot(v1, v1.T))
    print 'Eigen Value 1 : ', l1, 'Eigen Vector 1 : ', v1
    print 'Eigen Value 2 : ', l2, 'Eigen Vector 2 : ', v2
    ev = np.hstack([v1, v2])
    l, v = np.linalg.eig(B)
    ax = plt.axes()
    plt.scatter(A[0, :], A[1, :])
    ax.arrow(0, 0, v1[0][0], v1[1][0], head_width=0.05, head_length=0.1, fc='k', ec='k')
    ax.arrow(0, 0, v2[0][0], v2[1][0], head_width=0.05, head_length=0.1, fc='k', ec='k')
    plt.show()
