import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import MLSP.stft_try as stft

if __name__ == '__main__':
    piano_sampling_rate, piano_data = wavfile.read("piano.wav")
    fft_size = 1024
    window = np.hanning(fft_size)
    step = fft_size / 2

    S = stft.stft(piano_data, fft_size, step, window)

    # S = S.T
    # S = S[:513]
    # S = S.T
    print S.shape

    # plt.imshow(abs(S), aspect="auto", origin="lower")
    # plt.title("Piano Spectrogram")
    # plt.show()

    recovered = stft.istft(S, fft_size, step/2, window)

    wavfile.write('out_wav.wav', piano_sampling_rate, recovered)
