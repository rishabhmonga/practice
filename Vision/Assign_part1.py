from scipy.io import loadmat
from scipy.misc import imread, toimage
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import seaborn as sns
import pandas as pd

"""
from PIL import Image
import numpy as np
import scipy.fftpack as fp

## Functions to go from image to frequency-image and back
im2freq = lambda data: fp.rfft(fp.rfft(data, axis=0),
                               axis=1)
freq2im = lambda f: fp.irfft(fp.irfft(f, axis=1),
                             axis=0)

## Read in data file and transform
data = np.array(Image.open('test.png'))

freq = im2freq(data)
back = freq2im(freq)
# Make sure the forward and backward transforms work!
assert(np.allclose(data, back))

## Helper functions to rescale a frequency-image to [0, 255] and save
remmax = lambda x: x/x.max()
remmin = lambda x: x - np.amin(x, axis=(0,1), keepdims=True)
touint8 = lambda x: (remmax(remmin(x))*(256-1e-4)).astype(int)

def arr2im(data, fname):
    out = Image.new('RGB', data.shape[1::-1])
    out.putdata(map(tuple, data.reshape(-1, 3)))
    out.save(fname)

arr2im(touint8(freq), 'freq.png')
"""

if __name__ == '__main__':
    img = imread("noise1.png")
    img = np.array(img)
    img_dft = np.fft.fft2(img)

    # img_dft_real = img_dft.real
    # max_list = []
    # for i in img_dft_real:
    #     max_list.append(max(i))
    #
    # print max_list
    # df = pd.DataFrame(max_list)
    # print df.sort(ascending=False).head(20)

    img_dft[511] = np.zeros(np.shape(img_dft[0]))
    img_clear = np.fft.ifft2(img_dft)
    toimage(img_clear).save('clear.jpg')


