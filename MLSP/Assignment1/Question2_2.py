import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
import seaborn as sns
import EigenValue


def covariance(X):
    X -= X.mean(axis=0)
    N = X.shape[1]
    fact = float(N - 1)
    return np.dot(X, X.T.conj()) / fact


if __name__ == '__main__':
    A = loadmat('./flute.mat')['X']
    # sns.heatmap(A)
    # plt.show()

    n_cov = covariance(A)
    print n_cov.shape
    l1, v1 = EigenValue.eigen(n_cov)
    l2, v2 = EigenValue.eigen(n_cov - l1 * np.dot(v1, v1.T))
    print 'Eigen Value 1 : ', l1, 'Eigen Vector 1 : ', v1
    print 'Eigen Value 2 : ', l2, 'Eigen Vector 2 : ', v2
    plt.scatter(v1, v2)
    plt.show()

    ev = np.hstack((v1, v2)).T
    sns.heatmap(ev)
    plt.show()
    print A.shape, ev.shape
    projected = np.dot(ev, A)
    sns.heatmap(projected)
    plt.show()

    residual = np.zeros(A.shape)
    residual[:2] = np.add(residual[:2], projected)
    recovered = np.subtract(A, residual)
    #
    sns.heatmap(recovered)
    plt.show()
