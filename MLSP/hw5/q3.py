from __future__ import division
from scipy.io import wavfile
import stft_try as stft_try
import numpy as np
import matplotlib.pyplot as plt
import math


def get_snr(X, X_recovered):
    numerator = np.sum(np.square(X))
    denominator = np.sum(np.square(X - X_recovered))
    print("numerator : ", numerator)
    print("denominator : ", denominator)
    return 10 * math.log10(numerator / denominator)


def plsi(X, n=10):
    B = np.random.random((X.shape[0], 30))
    theta = np.random.random((30, X.shape[1]))
    for _ in range(n):
        b_theta = np.dot(B, theta)
        B = np.multiply(B, np.dot(np.divide(X, b_theta), theta.T))
        b_theta = np.dot(B, theta)
        theta = np.multiply(theta, np.dot(B.T, np.divide(X, b_theta)))
        one_v_v = np.ones((B.shape[0], B.shape[0]))
        B = np.divide(B, (np.dot(one_v_v, B)))
        one_k_k = np.ones((theta.shape[0], theta.shape[0]))
        theta = np.divide(theta, (np.dot(one_k_k, theta)))
    return B, theta

def update_theta(X, B, n=2000):
    theta = np.random.random((60, X.shape[1]))
    for _ in range(n):
        b_theta = np.dot(B, theta)
        theta = np.multiply(theta, np.dot(B.T, np.divide(X, b_theta)))
        one_k_k = np.ones((theta.shape[0], theta.shape[0]))
        theta = np.divide(theta, (np.dot(one_k_k, theta)))
    return theta


if __name__ == '__main__':
    s_sample, s = wavfile.read('data/trs.wav')
    n_sample, n = wavfile.read('data/trn.wav')

    tex_sample, tex = wavfile.read('data/tex.wav')
    tes_sample, tes = wavfile.read('data/tes.wav')

    x = s + n
    print(x.shape)

    frame_size = 1024
    hop_size = 512
    window = np.hanning(frame_size)

    s_spec = stft_try.stft(s, frame_size, hop_size, window)
    n_spec = stft_try.stft(n, frame_size, hop_size, window)
    x_spec = stft_try.stft(x, frame_size, hop_size, window)

    tex_spec = stft_try.stft(tex, frame_size, hop_size, window)[:513]
    tes_spec = stft_try.stft(tes, frame_size, hop_size, window)[:513]

    B_s, theta_s = plsi(s_spec.real)

    B_n, theta_n = plsi(n_spec.real)

    B = np.hstack((B_s, B_n))
    # theta = np.vstack((theta_s, theta_n))
    #
    # X = x_spec
    # Y = np.abs(X)

    theta_tex = update_theta(tex_spec.real, B)

    numerator = np.dot(B_s, theta_tex[:30])

    denominator = np.dot(B, theta_tex)

    M_bar = numerator / denominator

    tex_sig = np.multiply(tex_spec, M_bar)

    Y = tex_spec.real
    Y = np.abs(Y)

    tex_missing = tex_spec / Y

    tex_sig += tex_missing

    tex_recov = stft_try.istft(tex_sig, frame_size, hop_size, window)
    # tex_recov = istft2(tes_spec)

    wavfile.write('q3_out_wav_sig.wav', tes_sample, tex_recov)

    get_snr(tes_spec, tex_sig)