import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import math
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
    x[pos] /= wsum[pos]
    return x


def get_snr(X, X_recovered):
    numerator = np.sum(np.square(X))
    denominator = np.sum(np.square(X) - np.square(X_recovered))
    print "numerator : ", numerator
    print "denominator : ", denominator
    return 10 * math.log10(numerator / denominator)


def get_binary_mask(signal, noise):
    bin_mask = np.array(signal.shape)
    for row in xrange(len(signal)):
        for col in xrange(len(signal[0])):
            if signal[row][col] > noise[row][col]:
                bin_mask = 1
            else:
                bin_mask = 0
    return bin_mask


if __name__ == '__main__':
    piano_sampling_rate, piano_data = wavfile.read("piano.wav")
    ocean_sampling_rate, ocean_data = wavfile.read("ocean.wav")
    fft_size = 1024
    window = np.hanning(fft_size)
    step = fft_size / 2

    # S = stft(piano_data, window, step)
    S = st_try.stft(piano_data, fft_size, step, window)

    S = S.T
    S = S[:513]
    print S.shape

    # plt.imshow(abs(S), aspect="auto", origin="lower")
    # plt.title("Piano Spectrogram")
    # plt.show()

    # N = stft(ocean_data, window, step)
    N = st_try.stft(ocean_data, fft_size, step, window)
    N = N.T
    N = N[:513]
    print N.shape
    X = S + N

    M = S / (S + N)
    S_1 = np.multiply(M, X)

    M_bar = (S * S) / ((S * S) + (N * N))
    S_1 = np.multiply(M_bar, X)
    print "S_1 shape", S_1.shape

    # recovered = istft(S_1.T, S_1.shape[0], 513)
    recovered = st_try.istft(S_1.T, fft_size, step, window)


    print recovered.shape

    # wavfile.write('out_wav_S_1.wav', ocean_sampling_rate, recovered)
    wavfile.write('out_wav_S_1_compare.wav', ocean_sampling_rate, recovered)

    SNR = get_snr(S, S_1)
    print "SNR-1 : ", SNR
    IBM = get_binary_mask(S, N)
    S_2 = np.multiply(IBM, X)

    # recovered = istft(S_2.T, S_2.shape[0], 513)
    recovered = st_try.istft(S_2.T, fft_size, step, window)

    wavfile.write('out_wav_S_2_compare.wav', ocean_sampling_rate, recovered)
    SNR = get_snr(S, S_2)
    print "SNR-2 : ", SNR

