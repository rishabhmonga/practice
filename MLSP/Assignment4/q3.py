from scipy.io import loadmat
import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import seaborn

g = lambda x: 1 / (1 + np.exp(-x))


def kernel_transform(X):
    # pdist to calculate the squared Euclidean distances for every pair of points
    sq_dists = pdist(X, 'sqeuclidean')
    gamma = 0.7
    # gamma = 1
    mat_sq_dists = squareform(sq_dists)
    kernel = np.exp(-gamma * mat_sq_dists)
    val, vec = np.linalg.eigh(kernel)
    # val, vec = np.linalg.eigh(kernel)
    # # eigvals, eigvecs = zip(*sorted(zip(val, vec), reverse=True))

    # eigvals, eigvecs = zip(*sorted(zip(val, vec), reverse=True))

    # return eigvecs[0]
    return np.column_stack((vec[:, -i] for i in range(1, 4)))


def perceptron(Z, label, wt, eta, b, iterations=1000):
    for i in range(iterations):
        index = i % len(Z)
        err = label[index] - g(np.dot(Z[index].T, wt) + b)
        if err:
            wt += eta * err * Z[index]
            b += eta * err * np.mean(Z[index])
    return wt, b


def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0


if __name__ == '__main__':
    X = np.array(loadmat('data/concentric.mat')['X'])

    plt.plot(X[0], X[1])
    plt.show()

    Z = kernel_transform(X.T)
    plt.plot(Z)
    plt.show()
    #
    # fig = plt.figure()
    # ax = p3.Axes3D(fig)
    # ax.scatter(Z.T[0], Z.T[1], Z.T[2], cmap='plasma')
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z')
    # plt.show()

    labels = np.zeros(len(Z))

    for i in range(len(Z[0])):
        labels[i] = 0 if i < 51 else 1

    bias = 0
    # eta = 0.01
    eta = 0.1
    iterations_range = [5, 10, 100, 500, 1000, 5000, 10000]
    acc = {}
    for iterations in iterations_range:
        instant_acc = []
        for _ in range(5):
            weights = np.random.randn(len(Z[0])) - 0.5
            weights, bias = perceptron(Z, labels, weights, eta, bias, iterations)
            mat = np.zeros(labels.shape)
            for idx in range(len(Z)):
                mat[idx] = np.round(g(np.dot(Z[idx], weights) + bias))
            instant_acc.append(accuracy_metric(labels, mat))
        acc[iterations] = np.mean(instant_acc)

    lists = sorted(acc.items())
    ax_x, ax_y = zip(*lists)
    plt.plot(ax_x, ax_y)
    plt.show()
