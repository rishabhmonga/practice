import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import scipy


def stft(data, fs, fft_size, overlap_fac):
    hop_size = np.int32(np.floor(fft_size * (1 - overlap_fac)))
    pad_end_size = fft_size  # the last segment can overlap the end of the data array by no more than one window size
    total_segments = np.int32(np.ceil(len(data) / np.float32(hop_size)))
    t_max = len(data) / np.float32(fs)

    window = np.hanning(fft_size)  # our half cosine window
    inner_pad = np.zeros(fft_size)  # the zeros which will be used to double each segment size

    proc = np.concatenate((data, np.zeros(pad_end_size)))  # the data to process
    result = np.empty((total_segments, fft_size), dtype=np.float32)  # space to hold the result

    for i in xrange(total_segments):  # for each segment
        current_hop = hop_size * i  # figure out the current segment offset
        segment = proc[current_hop:current_hop + fft_size]  # get the current segment
        windowed = segment * window  # multiply by the half cosine function
        padded = np.append(windowed, inner_pad)  # add 0s to double the length of the data
        spectrum = np.fft.fft(padded) / fft_size  # take the Fourier Transform and scale by the number of samples
        autopower = np.abs(spectrum * np.conj(spectrum))  # find the autopower spectrum
        result[i, :] = autopower[:fft_size]  # append to the results array

    # result = 20 * np.log10(result)  # scale to db
    # result = np.clip(result, -40, 200)  # clip values
    return result

def stft_2(x, fftsize=1024, overlap=4):
    hop = fftsize / overlap
    w = np.hanning(fftsize+1)[:-1]      # better reconstruction with this trick +1)[:-1]
    return np.array([np.fft.rfft(w*x[i:i+fftsize]) for i in range(0, len(x)-fftsize, hop)])

# def istft(X, fs, T, hop):
#     x = np.zeros(T * fs)
#     framesamp = X.shape[1]
#     hopsamp = int(hop * fs)
#     for n, i in enumerate(range(0, len(x) - framesamp, hopsamp)):
#         x[i:i + framesamp] += np.fft.ifft(X[n]).real
#     return x

def istft(X, overlap=4):
    fftsize=(X.shape[1]-1)*2
    hop = fftsize / overlap
    # w = scipy.hanning(fftsize+1)[:-1]
    w = np.hanning(fftsize)
    x = scipy.zeros(X.shape[0]*hop)
    wsum = scipy.zeros(X.shape[0]*hop)
    for n,i in enumerate(range(0, len(x)-fftsize, hop)):
        x[i:i+fftsize] += np.fft.irfft(X[n]).real * w   # overlap-add
        wsum[i:i+fftsize] += w ** 2.
    pos = wsum != 0
    x[pos] /= wsum[pos]
    return x


if __name__ == '__main__':
    sampling_rate = 16000
    sig_original = wavfile.read("x.wav")
    sig_original = np.array(sig_original[1])

    result = stft(sig_original, 16000, 1600, 0.05)
    # result = stft_2(sig_original, fftsize=1600, overlap=4)
    print result.shape
    for i in xrange(len(result)):
        for j in xrange(len(result[i])):
            if 395 < j < 405:
                result[i][j] = 0

    spectrogram = plt.imshow(result, origin='lower', cmap='jet', interpolation='nearest', aspect='auto')
    plt.show()

    # sig_output = istft(result, 16000, 3, 0.05)
    sig_output = istft(result)
    plt.plot(sig_output)
    plt.show()
    # stft(x, 8000, 0.050, 0.025)
    # istft(x, 8000, 5, 0.025)




    # out_wav = wavfile.write('out_wav.wav', sampling_rate, sig_output)
