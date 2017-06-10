from __future__ import division
from scipy.io import loadmat
from scipy.misc import imread, toimage
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math


def g_fx(x):
    return 1. / (1. + np.exp(-x))

def g_dash_fx(x):
    return g_fx(x) * (1. - g_fx(x))

def get_img_and_data_matrix(img, f):
    img_small = img[:186, :186]
    img_small = img_small.ravel()
    data_matrix = np.random.random((225, 186 * 186))
    for i in range(len(f)):
        data_matrix[i] = img_small
    temp = list()
    temp.append(img_small)
    img_small = np.array(temp)
    return img_small.T, data_matrix

def gradient_desc(img, f, N):
    eta = 1
    s, data_matrix = get_img_and_data_matrix(img, f)
    errors = []
    for i in range(N):
        ft_X = np.dot(f.T, data_matrix)
        g_vec = g_fx(ft_X)
        s_T_minus_g_vec = s.T - g_vec
        g_vec_dash = g_dash_fx(ft_X)
        hadamard_product = np.multiply(s_T_minus_g_vec, g_vec_dash)
        error = -(2/186.)* np.sum( np.dot(data_matrix, hadamard_product.T))
        f += eta * np.fabs(error)
        print 'iterations done : ', i, error
        errors.append(error)

    s_new = np.dot(f.T, data_matrix)
    s_new = s_new.reshape((186, 186))
    return s_new, errors, f

if __name__ == '__main__':
    iterations = 2000
    train_clear = imread('./sg_train.jpg')
    train_clear = train_clear/255.0
    train_clear = train_clear[:186, :186]

    noisy_train = imread('./sgx_train.jpg')
    test_image_bw = noisy_train / 255.0
    f = np.random.uniform(low=0.001, high=1, size=(225, 1))
    filtered_image, errors, f = gradient_desc(test_image_bw, f, iterations)

    diff_img = np.subtract(test_image_bw[:186, :186], filtered_image)

    # toimage(filtered_image).save('.\pics\outfile' + str(iterations) + '.jpg')
    # toimage(diff_img).save('.\pics\diff' + str(iterations) + '.jpg')

    test_image = imread('./sgx_test.jpg')
    test_image = test_image / 255.0
    test_image = test_image[:186, :186]
    test_data = get_img_and_data_matrix(test_image, f)[1]

    filtered_test_image = np.dot(f.T, test_data)
    filtered_test_image = filtered_test_image.reshape((186, 186))


    # bad_image = np.subtract(test_image, diff_img)
    # toimage(filtered_test_image).save('.\pics\check' + str(iterations) + '.jpg')
    # plt.plot(errors)
    plt.imshow(filtered_test_image)
    plt.gray()
    #
    plt.show()
