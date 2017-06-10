import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.io import  loadmat
from scipy.spatial.distance import pdist, squareform
from scipy.linalg import eigh
import mpl_toolkits.mplot3d.axes3d as p3

concentric = loadmat("data/concentric.mat")

X = concentric['X']
X = np.array(X, dtype=float)

#concentric circles
#plt.plot(X[0], X[1])
#plt.show()

X = X.T

#kernel Function = RBF

def rbf_kernel(x):


    distance = pdist(x, 'sqeuclidean')
    mat_distance = squareform(distance)

    # Computing the MxM kernel matrix.
    K = np.exp(-1 * mat_distance)


    # Obtaining eigenvalues in descending order with corresponding
    # eigenvectors from the symmetric matrix.
    eigvals, eigvecs = np.linalg.eigh(K)

    # Obtaining the i eigenvectors that corresponds to the i highest eigenvalues.
    x_pc = np.column_stack((eigvecs[:, -i] for i in range(1, 3+1)))

    return x_pc

X = rbf_kernel(X)
X = X.T

fig=plt.figure()
ax = p3.Axes3D(fig)
ax.plot_wireframe(X[0], X[1], X[2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# plt.show()

# Apply percceptron

X = X.T
rows, cols = X.shape  # 152x3
y = np.zeros(rows)

# If first 51 samples = 0, else 1
for i in range(cols):
    if (i < 51):
        y[i] = 0

    else:
        y[i] = 1

bias = 0
eta = 0.01
epochs = 1520  # 3040

# random weight
W = np.random.randn(cols) - 0.5


# print(W)
# print(W.shape, X.shape, y.shape)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def perceptron(X, y, W, epochs, eta, bias):
    for i in range(epochs):

        idx = i % rows

        activation = sigmoid(np.dot(X[idx].T, W) + bias)
        error = y[idx] - activation
        # print(error)
        # print(error, X[idx].shape, W.shape)

        if (error != 0):
            W += eta * (error) * X[idx]
            bias += eta * error * np.mean(X[idx])

    return W, bias


W, bias = perceptron(X, y, W, epochs, eta, bias)

print(W,bias, "two")

# test
accuracy = 0

for i in range(rows):
    activation = np.round(sigmoid(np.dot(X[i], W) + bias))
    error = y[i] - activation

    if (error == 0):
        accuracy += 1

print(accuracy / rows * 100)


















# #Apply percceptron
#
# rows, cols = X.shape  # 3x152
# y = np.zeros(cols)
#
# # If first 51 samples = 0, else 1
# for i in range(cols):
#     if (i < 51):
#         y[i] = 0
#
#     else:
#         y[i] = 1
#
# bias = 0
# eta = 0.01
# epochs = 1520
#
# # random weight
# W = np.random.randn(cols)
#
#
# # print(W)
# # print(W.shape, X.shape, y.shape)
#
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
#
#
# def perceptron(X, y, W, epochs, eta, bias):
#     for i in range(epochs):
#
#         idx = i % rows
#
#         activation = sigmoid(np.dot(X[idx], W) + bias)
#         error = y[idx] - activation
#
#         # print(error, X[idx].shape, W.shape)
#
#         if (error != 0):
#             W += eta * (error) * X[idx]
#             bias += eta * error * np.mean(X[idx])
#
#     return W, bias
#
#
# W, bias = perceptron(X, y, W, epochs, eta, bias)
#
# # print(W,bias, "two")
#
# # test
# accuracy = 0
#
# for i in range(rows):
#     activation = np.round(sigmoid(np.dot(X[i], W) + bias))
#     error = y[i] - activation
#
#     if (error == 0):
#         accuracy += 1
#
# print(accuracy / rows * 100)