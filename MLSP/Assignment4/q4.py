from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import seaborn


def plot_decision_boundary(pred_func):
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z)
    plt.scatter(X[:, 0], X[:, 1])


def get_model_loss(model):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    correct_logprobs = -np.log(probs[range(num_examples), y])
    data_loss = np.sum(correct_logprobs)
    data_loss += reg_lambda / 2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
    return 1. / num_examples * data_loss


def predict(model, x):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    z1 = x.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return np.argmax(probs, axis=1)


def generate_neural_net(hidden_dim, iterations=20000, print_loss=False):
    np.random.seed(0)
    W1 = np.random.randn(nn_input_dim, hidden_dim) / np.sqrt(nn_input_dim)
    b1 = np.zeros((1, hidden_dim))
    W2 = np.random.randn(hidden_dim, nn_output_dim) / np.sqrt(hidden_dim)
    b2 = np.zeros((1, nn_output_dim))

    model = {}
    losses = []

    for i in range(0, iterations):

        z1 = X.dot(W1) + b1
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

        # backpropagation
        delta3 = probs
        delta3[range(num_examples), y] -= 1
        dW2 = (a1.T).dot(delta3)
        db2 = np.sum(delta3, axis=0, keepdims=True)
        delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))
        dW1 = np.dot(X.T, delta2)
        db1 = np.sum(delta2, axis=0)

        dW2 += reg_lambda * W2
        dW1 += reg_lambda * W1

        W1 += -eta * dW1
        b1 += -eta * db1
        W2 += -eta * dW2
        b2 += -eta * db2

        model = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}

        if print_loss and i % 1000 == 0:
            loss = get_model_loss(model)
            print("Loss after iteration: ", i, ' : ', loss)
            losses.append(loss)
        elif not print_loss:
            print("Loss : ", get_model_loss(model))
    plt.plot(losses)
    plt.show()
    return model


if __name__ == '__main__':
    X = np.array(loadmat('data/concentric.mat')['X']).T

    y = np.array([0] * 51 + [1] * 101)
    # plt.scatter(X[:, 0], X[:, 1])
    # plt.show()
    #
    num_examples = len(X)
    nn_input_dim = 2
    nn_output_dim = 2

    eta = 0.01
    reg_lambda = 0.01

    model = generate_neural_net(10, iterations=10000, print_loss=True)
    #
    # plot_decision_boundary(lambda x: predict(model, x))
    # plt.show()

