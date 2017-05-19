from numpy.linalg import svd
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import scipy.sparse as sparse

if __name__ == '__main__':
    mds_mat = np.matrix(loadmat('data/MDS_pdist.mat')['L'])

    # row_avgs = []
    # for i in range(len(mds_mat)):
    #     row_avgs.append(np.mean(mds_mat[i]))
    # row_avgs = np.array(row_avgs)
    #
    # m_row = []
    # for i in range(len(mds_mat)):
    #     m_row.append(mds_mat[i] - row_avgs[i])
    # m_row = np.array(m_row)
    #
    # col_avgs = []
    # m_row_t = m_row.T
    # for i in range(len(m_row_t)):
    #     col_avgs.append(np.mean(m_row_t[i]))
    # col_avgs = np.array(col_avgs)
    #
    # m_col = []
    # for i in range(len(m_row_t)):
    #     m_col.append(m_row_t[i] - col_avgs[i])
    # m_col = np.array(m_col)
    #
    # w = (-1 / 2) * (m_row - m_col)
    #
    # # val, vec = np.linalg.eig(w)
    #
    #


    row_avgs = mds_mat.mean(0)
    m_row = mds_mat-row_avgs
    col_avgs = m_row.mean(1)

    w = (-1/2)*(m_row - col_avgs)

    # print(w.shape)
    y = np.dot(w.T, w)

    val, vec = sparse.linalg.eigs(y, k=2)

    plt.scatter(vec[:, 0], vec[:, 1])
    plt.show()

    # [U, V, UT] = svd(w)
    #
    #
    #
    # U = np.array(U)
    # Y = U * np.sqrt(V)
    #
    # Y = Y[:, 0:2]
    # plt.scatter(Y[:, 0], Y[:, 1], cmap=plt.cm.Spectral)
    #
    # plt.show()

"""
    # eigenValues, eigenVectors = np.linalg.eig(w)

    # idx = eigenValues.argsort()[::-1]
    # eigenValues = eigenValues[idx]
    # eigenVectors = eigenVectors[:, idx]


    # print(vec[0].shape)
    # plt.scatter(eigenVectors[0], eigenVectors[1])
    # plt.show()

"""