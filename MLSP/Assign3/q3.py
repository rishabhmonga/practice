from __future__ import division
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import math


def stft(x, window, step):
    l = len(x)  # input signal length
    n = len(window)  # window length
    m = int(np.ceil(float(l - n + step) / step))

    new_x = np.zeros(n + ((m - 1) * step))
    new_x[:l] = x

    X = np.zeros([m, n], dtype=complex)
    for m in range(m):
        start = step * m
        X[m, :] = np.fft.fft(new_x[start: start + n] * window)
    return X


def istft(X, win, step):
    M, N = X.shape
    l = (M - 1) * step + N
    x = np.zeros(l, dtype=float)
    wsum = np.zeros(l, dtype=float)
    for m in range(M):
        start = step * m
        x[start: start + N] = x[start: start + N] + np.fft.ifft(X[m, :]).real * win
        wsum[start: start + N] += win ** 2
    pos = (wsum != 0)
    x[pos] /= wsum[pos]
    return x


def nmf(spectrogram):
    """
    W = mult(W, (X.H_T)/(W.H.H_T))
    H = mult(H, (W_T.X)/(W_T.W.H))
    :param spectrogram: 
    :return: 
    """
    W = np.random.random((spectrogram.shape[0], 30))
    H = np.random.random((30, spectrogram.shape[1]))
    for _ in xrange(1000):
        W = np.multiply(W, np.dot(spectrogram, H.T) / np.dot(W, np.dot(H, H.T)))
        H = np.multiply(H, np.dot(W.T, spectrogram) / np.dot(np.dot(W.T, W), H))
    return W, H


# def get_snr(W_S, W, H):
#     """
#     (W_S.H[:30])/(W.H)
#     :return:
#     """
#     mask = np.dot(W_S, H[:30])/np.dot(W, H)


if __name__ == '__main__':
    speech_sampling_rate, speech_data = wavfile.read("trs.wav")
    noise_sampling_rate, noise_data = wavfile.read("trn.wav")
    x_sampling_rate, x_data = wavfile.read("x_nmf.wav")
    fft_size = 1024
    window = np.hanning(fft_size)
    step = fft_size / 2

    speech_spectrogram = stft(speech_data, window, step)
    noise_spectrogram = stft(noise_data, window, step)
    x_spectrogram = stft(x_data, window, step)
    # plt.imshow(abs(spectrogram), aspect="auto", origin="lower")
    # plt.title("Spectrogram")
    # plt.show()

    W_S = []
    W_N = []

    X = np.abs(x_spectrogram)
    X = X.T
    X = X[:513]

    W = np.hstack((W_S, W_N))

    H = np.random.random((60, 129))

    for _ in range(100):
        J = np.dot(W, np.dot(H, H.T)) - np.dot(X, H.T)
        H = np.multiply(H, np.dot(W.T, X) / np.dot(np.dot(W.T, W), H))

    print("H.shape: ", H.shape)
