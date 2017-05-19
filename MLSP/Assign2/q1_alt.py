import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import MLSP.stft_try as st_try


def stft(x, window, step):
    l = len(x)  # input signal length
    n = len(window)  # window length
    m = int(np.ceil(float(l - n + step) / step))

    new_x = np.zeros(n + ((m - 1) * step))
    new_x[:l] = x

    X = np.zeros([m, n], dtype=complex)
    for m in xrange(m):
        start = step * m
        X[m, :] = np.fft.fft(new_x[start: start + n] * window)
    return X


def istft(X, win, step):
    M, N = X.shape
    l = (M - 1) * step + N
    x = np.zeros(l, dtype=float)
    wsum = np.zeros(l, dtype=float)
    for m in xrange(M):
        start = step * m
        x[start: start + N] = x[start: start + N] + np.fft.ifft(X[m, :]).real * win
        wsum[start: start + N] += win ** 2
    pos = (wsum != 0)
    # x_pre = x.copy()
    x[pos] /= wsum[pos]
    return x


if __name__ == '__main__':
    sampling_rate, data = wavfile.read("x.wav")
    fft_size = 1600
    window = np.hamming(fft_size)
    step = fft_size / 4

    spectrogram = stft(data, window, step)

    # plt.plot(spectrogram)
    # plt.show()

    spectrogram = st_try.stft(data, fft_size, step, window)

    # for i in range(len(spectrogram)):
    #     j = np.argmax(spectrogram[i])
    #     if spectrogram[i][j].real > 800000:
    #         print i, j, spectrogram[i][j]

    # for i in xrange(len(spectrogram)):
    #     if 55 < i < 65 or 85 < i < 95:
    #         spectrogram[i] = np.zeros(spectrogram[i].shape)

    for i in xrange(len(spectrogram)):
        for j in xrange(len(spectrogram[0])):
            if 198 < j < 202 or 1398 < j < 1402:
                spectrogram[i][j] = 0

    # recovered = istft(spectrogram, window, step)

    recovered = st_try.istft(spectrogram, fft_size, step, window)

    plt.imshow(abs(spectrogram[:, : fft_size / 2 + 1]), aspect="auto", origin="lower")
    # plt.imshow(abs(spectrogram), aspect="auto", origin="lower")
    plt.title("Spectrogram")
    plt.show()

    wavfile.write('out_wav.wav', sampling_rate, recovered)
