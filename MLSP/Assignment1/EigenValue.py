import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat


def get_eigen_value(matrix):
    return np.linalg.eigvals(matrix)


def eigen(A, n=100):
    eest = np.zeros((n, 1))
    v = np.random.random((A.shape[1], 1))
    for i in range(n):
        x = np.dot(A, v)
        e = np.dot(x.T, v) / np.dot(v.T, v)
        v = x / np.linalg.norm(x, ord='fro')
        eest[i] = e
    return eest[n - 1][0], v


if __name__ == '__main__':
    A = loadmat('./X.mat')['X']
    A = np.array(A)
    X = np.dot(A, A.T)
    l_1, v_1 = eigen(X)
    print('L_1', l_1)
    print('V_1', v_1)
    B = X - l_1 * np.dot(v_1, v_1.T)
    l_2, v_2 = eigen(B)
    print('L_2', l_2)
    print('V_2', v_2)
    plt.plot(v_1)
    plt.plot(v_2)
