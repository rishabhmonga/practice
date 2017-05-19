from __future__ import division
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import math


def format_eigen_matrix(mat):
    mat = mat.T[0]
    eig_vec = mat
    for i in range(len(mat)):
        eig_vec[i] = np.flipud(mat[i])
    return eig_vec


def get_eigen_vectors(A, n=8):
    eigen_vectors = []
    eigen_values = []
    X = A
    for _ in range(n):
        l, v = eigen(X)
        eigen_vectors.append(v)
        eigen_values.append(l)
        X = X - l * np.dot(v, v.T)
    return np.array(eigen_values), np.array(eigen_vectors)


def eigen(A, n=100):
    eest = np.zeros((n, 1))
    v = np.random.random((A.shape[1], 1))
    for i in range(n):
        x = np.dot(A, v)
        e = np.dot(x.T, v) / np.dot(v.T, v)
        v = x / np.linalg.norm(x, ord='fro')
        eest[i] = e
    return eest[n - 1][0], v


def fx(x):
    return np.power(x, 3)


def g_fx(x):
    return np.tanh(x)


def get_whitened_input(Y):
    cov = np.cov(Y)
    lmbda, vec = get_eigen_vectors(cov, n=4)
    lmbda = np.flipud(lmbda)
    eig_vec = format_eigen_matrix(vec)
    print lmbda.shape
    print eig_vec.shape
    lmbda_matrix = np.diag(lmbda)

    lmbda_inverse = np.sqrt(np.linalg.inv(lmbda_matrix))
    print lmbda_inverse.shape
    return np.dot(lmbda_inverse, np.dot(eig_vec.T, Y))


def get_W_matrix(N, Z):
    mat = np.multiply(N, Z)
    cov = np.cov(mat)
    vec = get_eigen_vectors(cov, n=4)[1]
    return format_eigen_matrix(vec)


if __name__ == '__main__':
    x_1_sampling, x_1_data = wavfile.read("x_ica_1.wav")
    x_2_sampling, x_2_data = wavfile.read("x_ica_2.wav")
    x_3_sampling, x_3_data = wavfile.read("x_ica_3.wav")
    x_4_sampling, x_4_data = wavfile.read("x_ica_4.wav")

    Y = np.vstack((x_1_data, x_2_data, x_3_data, x_4_data))
    Y = np.array(Y, dtype=np.double)
    Z = get_whitened_input(Y)
    N = np.array([np.linalg.norm(Z, axis=0)] * 4)
    W = get_W_matrix(N, Z)

    rho = 10 ** -7

    for i in range(1):
        Y = np.dot(W, Z)
        Y = Y / np.max(Y)  # preventing overflow by normalizing
        delta_W = (4 * np.identity(4) - np.dot(g_fx(Y), fx(Y).T)) * rho
        W = W + delta_W

    output = np.dot(W.T, Z)
    # print output.shape

    # wavfile.write('ica_out_1.wav', x_1_sampling, output[0])
    # wavfile.write('ica_out_2.wav', x_2_sampling, output[1])
    # wavfile.write('ica_out_3.wav', x_3_sampling, output[2])
    # wavfile.write('ica_out_4.wav', x_4_sampling, output[3])
