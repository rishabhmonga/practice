from scipy.io import loadmat
import numpy as np


def plsi(X, n=1000):
    B = np.random.random((X.shape[0], 50))
    theta = np.random.random((50, X.shape[1]))
    ep = 10e-3
    for _ in xrange(n):
        b_theta = np.dot(B, theta)
        B = np.multiply(B, np.dot(np.divide(X + ep, b_theta + ep), theta.T))
        b_theta = np.dot(B, theta)
        theta = np.multiply(theta, np.dot(B.T, np.divide(X + ep, b_theta + ep)))
    return B, theta


def update_theta(X, B, n=1000):
    theta = np.random.random((50, X.shape[1]))
    ep = 10e-3
    for _ in xrange(n):
        b_theta = np.dot(B, theta)
        theta = np.multiply(theta, np.dot(B.T, np.divide(X + ep, b_theta + ep)))
    return theta


def g(x):
    if x.ndim == 1:
        x = x.reshape((1, -1))
    max_x = np.max(x, axis=1).reshape((-1, 1))
    exp_x = np.exp(x - max_x)
    return exp_x / np.sum(exp_x, axis=1).reshape((-1, 1))

def perceptron(Z, label, W, b, epochs=1000):
    eta = 10e-5
    for _ in range(epochs):
        prediction = g(np.dot(Z.T, W) + b)
        delta = np.array(label.T - prediction, dtype=float)
        r, c = delta.shape
        for idx1 in range(r):
            for idx2 in range(c):
                if delta[idx1][idx2] < 0:
                    W = np.add(W, eta * np.dot(Z, delta))
                    b = np.add(b, eta * delta)
    return W, b


def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        for j in range(len(actual[0])):
            if actual[i][j] == predicted[i][j]:
                correct += 1
    return correct / float(len(actual) * len(actual[0])) * 100.0


if __name__ == '__main__':
    Xtr = loadmat('data/twitter.mat')['Xtr']
    Xte = loadmat('data/twitter.mat')['Xte']
    Ytr = loadmat('data/twitter.mat')['YtrMat']
    Yte = loadmat('data/twitter.mat')['YteMat']

    epochs = 100

    B, theta = plsi(Xtr, epochs)
    theta_test = update_theta(Xte, B, epochs)

    print 'learning'

    epochs = 5000
    Weight = np.random.randn(50, 3)
    b = np.empty_like(Ytr.T)
    Weight, b = perceptron(theta, Ytr, Weight, b, epochs)
    predicted = np.round(g(np.dot(theta.T, Weight) + b))
    print accuracy_metric(Ytr.T, predicted)

    # Training : 54.376886589

    epochs = 5000
    Weight = np.random.randn(50, 3)
    b = np.empty_like(Yte.T)
    Weight, b = perceptron(theta_test, Yte, Weight, b, epochs)
    predicted = np.round(g(np.dot(theta_test.T, Weight) + b))
    print accuracy_metric(Yte.T, predicted)

    # Test : 52.677029361

