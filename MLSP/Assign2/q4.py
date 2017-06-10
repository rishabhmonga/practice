import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random
import seaborn as sns


def getRandomRows(channel, rows):
    # getting random blocks from red
    rand = random.randint(1, rows - 8)
    random_rows = []

    for i in range(rand, rand + 8):
        random_rows.append(channel[i])

    random_rows = np.array(random_rows)

    return random_rows


def covariance(X):
    X -= X.mean(axis=0)
    N = X.shape[1]
    fact = float(N - 1)
    return np.dot(X, X.T.conj()) / fact


def get_R(img, rows, n):
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]

    to_concat = []
    for mat in [r, g, b]:
        for _ in range(n):
            to_concat.append(getRandomRows(mat, rows))
    R = np.concatenate(to_concat, axis=1)
    print R.shape

    return R


def get_eigen_vectors(A, n=8):
    eigen_vectors = []
    X = A
    for _ in range(n):
        l, v = eigen(X)
        eigen_vectors.append(v)
        X = X - l * np.dot(v, v.T)
    return np.array(eigen_vectors)


def eigen(A, n=100):
    eest = np.zeros((n, 1))
    v = np.random.random((A.shape[1], 1))
    for i in range(n):
        x = np.dot(A, v)
        e = np.dot(x.T, v) / np.dot(v.T, v)
        v = x / np.linalg.norm(x, ord='fro')
        eest[i] = e
    return eest[n - 1][0], v


def two_dim_DCT(X):
    """
    http://en.wikipedia.org/wiki/Discrete_cosine_transform#Multidimensional_DCTs
    http://en.wikipedia.org/wiki/JPEG#Discrete_cosine_transform
    """
    result = np.zeros(X.shape)
    N1, N2 = X.shape

    def alpha(n):
        if n == 0:
            return 0.353553390593  # sqrt(1/8.)
        else:
            return .5  # sqrt(2/8.)

    for (k1, k2), _ in np.ndenumerate(X):
        sub_result = 0.
        for n1 in range(N1):
            for n2 in range(N2):
                sub_result += X[n1, n2] * np.cos((np.pi / N1) * (n1 + .5) * k1) * np.cos((np.pi / N2) * (n2 + .5) * k2)
        result[k1, k2] = alpha(k1) * alpha(k2) * sub_result
    return result


def pca(img, rows, n):
    R = get_R(img, rows, n)
    R = R - R.mean()
    cov = covariance(R)
    w = get_eigen_vectors(cov)
    return w.T[0], R


if __name__ == '__main__':
    input_img = Image.open('IMG_1878.jpg')
    img_rows, img_cols = input_img.size
    input_img = np.asarray(input_img)

    w_T, R = pca(input_img, img_rows, 3)
    sns.heatmap(w_T)
    plt.show()

    dct_matrix = two_dim_DCT(covariance(R))
    sns.heatmap(dct_matrix)
    plt.show()

    w_T, R = pca(input_img, img_rows, 10)
    sns.heatmap(w_T)
    plt.show()

    dct_matrix = two_dim_DCT(covariance(R))
    sns.heatmap(dct_matrix)
    plt.show()
