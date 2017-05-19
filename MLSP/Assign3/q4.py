from __future__ import division

from collections import Counter

from scipy.io import loadmat
import matplotlib.pyplot as plt
import operator
import numpy as np
import math


def get_dist(point, train_row_1, train_row_2, train_label, k):
    distances = []
    for idx in xrange(len(train_row_1)):
        dist_1 = np.linalg.norm(point - train_row_1[idx])
        dist_2 = np.linalg.norm(point - train_row_2[idx])
        dist = min(dist_1, dist_2)
        distances.append((dist, train_label[idx]))
        # distances = distances[:k+2]
    distances.sort(key=operator.itemgetter(0))
    distances = distances[:k]
    return np.array(distances)


def get_neighbors(train_row_1, train_row_2, test_data, train_label, k):
    distances = [[0 for i in range(len(test_data[0]))] for j in range(len(test_data))]
    for idx in xrange(len(test_data)):
        for jdx in xrange(len(test_data[0])):
            distances[idx][jdx] = get_dist(test_data[idx][jdx], train_row_1, train_row_2, train_label, k)
    return np.array(distances)


def get_class_label(point):
    labels = [0, 0]
    for i in range(len(point)):
        if point[i][1] == 1:
            labels[0] += point[i][0]*0.5
        if point[i][1] == 2:
            labels[1] += point[i][0]*0.5
    return 1 if np.argmin(labels) == 0 else 2


def get_test_predictions(neightbors):
    predictions = [[0 for i in range(len(neightbors[0]))] for j in range(len(neightbors))]
    for idx in xrange(len(neightbors)):
        for jdx in xrange(len(neightbors[0])):
            predictions[idx][jdx] = get_class_label(neightbors[idx][jdx])
    return np.array(predictions)


def knn(train_row_1, train_row_2, test_data, train_label, k=5):
    neightbors = get_neighbors(train_row_1, train_row_2, test_data, train_label, k)
    test_predictions = get_test_predictions(neightbors)
    return test_predictions


def accuracy(predicted_labels, test_labels):
    correct = 0
    count = 0
    for i in range(len(predicted_labels)):
        for j in range(len(predicted_labels[0])):
            if predicted_labels[i][j] == test_labels[j]:
                correct += 1
            count += 1
    return (correct / count) * 100


# def stft(x, fftsize=64):
#     hop = 48
#     w = np.blackman(fftsize + 1)[:-1]
#     return np.array([np.fft.rfft(w * x[i:i + fftsize]) for i in range(0, len(x) - fftsize, hop)])


def stft(x, window=np.blackman(64), step=48):
    l = len(x)  # input signal length
    n = len(window)  # window length
    m = int(np.ceil(float(l - n + step) / step))

    new_x = np.zeros(n + ((m - 1) * step))
    new_x[:l] = x

    X = np.zeros([m, int(n/2)+1], dtype=complex)
    for m in xrange(m):
        start = step * m
        X[m, :] = np.fft.rfft(new_x[start: start + n] * window)
    return X


def get_data_matrix(data):
    c_3 = data[:, 0, :]
    c_z = data[:, 1, :]
    c_4 = data[:, 2, :]

    # fft_size = 64
    # window = np.blackman(fft_size)
    # step = 48
    # #
    # spectrogram_3 = stft(c_3.T[0])
    # print spectrogram_3.shape
    # exit()

    # data_matrix = list()
    # for i in xrange(len(c_3[0])):
    #     arr = list()
    #
    #     spectrogram_3 = stft2(c_3.T[i])
    #     arr.append(spectrogram_3.T[2:7])
    #     spectrogram_z = stft2(c_z.T[i])
    #     arr.append(spectrogram_z.T[2:7])
    #     spectrogram_4 = stft2(c_4.T[i])
    #     arr.append(spectrogram_4.T[2:7])
    #
    #     input_sample = np.array(arr).flatten()
    #     data_matrix.append(input_sample)

    data_matrix = list()
    for i in xrange(len(c_3[0])):
        arr = list()

        spectrogram_3 = stft(c_3.T[i])
        arr.append(spectrogram_3.T[2:7])
        spectrogram_z = stft(c_z.T[i])
        arr.append(spectrogram_z.T[2:7])
        spectrogram_4 = stft(c_4.T[i])
        arr.append(spectrogram_4.T[2:7])

        input_sample = np.array(arr).flatten()
        data_matrix.append(input_sample)

    return np.array(data_matrix).T


def get_Z_matrix(data_matrix):
    data_matrix = data_matrix - data_matrix.mean()
    cov = np.cov(data_matrix)

    l, v = np.linalg.eigh(cov)

    # v = v[:, :-70:-1]

    v = v[:,-10:-1]

    # plt.plot(l)
    # plt.show()

    return np.dot(v.T, data_matrix)


# def stft2(data, fft_size=64, win=64):
#     hop_size = 48
#     window = np.blackman(win)
#     total_segments = np.int32(np.ceil(len(data) / np.float32(hop_size)))
#     inner_pad = np.zeros((fft_size * 2) - win)
#     pad_end_size = fft_size
#
#     proc = np.concatenate((data, np.zeros(pad_end_size)))
#     result = np.empty((total_segments, fft_size), dtype=np.float32)
#
#     for i in xrange(total_segments):
#         current_hop = hop_size * i
#         segment = proc[current_hop:current_hop + win]
#         windowed = segment * window
#         padded = np.append(windowed, inner_pad)
#         spectrum = np.fft.fft(padded) / fft_size
#         autopower = np.abs(spectrum * np.conj(spectrum))
#         result[i, :] = autopower[:fft_size]
#
#     return result
#

if __name__ == '__main__':
    x_train = loadmat("eeg.mat")['x_train']
    x_test = loadmat("eeg.mat")['x_te']
    y_train = loadmat("eeg.mat")['y_train']
    y_test = loadmat("eeg.mat")['y_te']

    data_matrix_x_train = get_data_matrix(x_train)
    Z_x_train = get_Z_matrix(data_matrix_x_train)

    # print Z_x_train.shape

    data_matrix_x_test = get_data_matrix(x_test)
    Z_x_test = get_Z_matrix(data_matrix_x_test)

    # print Z_x_test.shape

    # Z_x_test = Z_x_test[1:4]

    ks = [3, 5, 13, 19, 25, 31, 45, 61, 71, 85]
    for k in ks:
        acc = []
        dist = knn(Z_x_train[1], Z_x_train[2], Z_x_test, y_train, k)
        acc.append(accuracy(dist, y_test))
        dist = knn(Z_x_train[3], Z_x_train[4], Z_x_test, y_train, k)
        acc.append( accuracy(dist, y_test))
        dist = knn(Z_x_train[5], Z_x_train[6], Z_x_test, y_train, k)
        acc.append( accuracy(dist, y_test))
        dist = knn(Z_x_train[7], Z_x_train[8], Z_x_test, y_train, k)
        acc.append( accuracy(dist, y_test))
        dist = knn(Z_x_train[1], Z_x_train[3], Z_x_test, y_train, k)
        acc.append( accuracy(dist, y_test))
        dist = knn(Z_x_train[2], Z_x_train[4], Z_x_test, y_train, k)
        acc.append( accuracy(dist, y_test))
        dist = knn(Z_x_train[5], Z_x_train[7], Z_x_test, y_train, k)
        acc.append( accuracy(dist, y_test))
        dist = knn(Z_x_train[6], Z_x_train[8], Z_x_test, y_train, k)
        acc.append( accuracy(dist, y_test))

        print k, ": ", max(acc)
    # print dist
    # print "predict: ", y_train.T, y_train.shape
    # print "correct: ", y_test.T
    # print accuracy(dist, y_test)
