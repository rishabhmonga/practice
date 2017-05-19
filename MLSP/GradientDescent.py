from __future__ import division
from scipy.io import loadmat
from scipy.misc import imread, toimage
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math


def g_element_wise(x):
    return 1 / (1 + np.exp(-x))


def g_fx(X):
    g = np.vectorize(g_element_wise)
    # applt on all elems
    g_of_X = g(X)
    return g_of_X.T


def g_dash_fx(x):
    return g_fx(x) * (1 - g_fx(x))


def get_img_and_data_matrix(img, f):
    img_small = img[:186, :186]
    img_small = img_small.ravel()
    data_matrix = np.random.random((225, 186 * 186))
    for i in range(len(f)):
        data_matrix[i] = img_small
    temp = list()
    temp.append(img_small)
    img_small = np.array(temp)
    return img_small, data_matrix


def gradient_desc(img, f, N):
    eta = 0.1
    s, data_matrix = get_img_and_data_matrix(img, f)
    # delta_f = np.array()
    errors = list()
    for i in range(N):
        ft_X = np.dot(f.T, data_matrix)
        print ft_X.shape

        g_vec = g_fx(ft_X)
        # g_vec = g_vec.T

        s_T_minus_g_vec = np.subtract(s.T, g_vec)
        print s_T_minus_g_vec.shape

        g_vec_dash = g_dash_fx(ft_X)

        hadamard_product = np.multiply(s_T_minus_g_vec, g_vec_dash)
        error = -(2 / 186.) * np.sum(np.dot(data_matrix, hadamard_product))
        errors.append(error)
        f = f + eta * np.abs(error)
        print 'iterations done : ', i, error
        # error = np.dot(data_matrix, hadamard_product)
        # error = error*(-2/186)
        # print np.mean(error)
        # f_new = np.add(f, error)
        # f = f_new
        print 'iterations done : ', i

    print 'data_matrix shape : ', data_matrix.shape
    print 'f.T shape : ', f.T.shape
    s_new = np.dot(f.T, data_matrix)
    s_new = s_new.reshape((186, 186))
    print s_new.shape
    return s_new, errors


if __name__ == '__main__':
    N = 500
    # test_image = imread('./sgx_test.jpg')

    test_image = imread('./sgx_train.jpg')

    test_image_bw = test_image / 255.0
    # test_image_bw = test_image
    # f = np.random.random((225, 1))
    f = np.ones((225, 1))
    filtered_image, errors = gradient_desc(test_image_bw, f, N)

    test_small = test_image_bw[:186, :186]
    diff_img = np.subtract(test_small, filtered_image)

    toimage(diff_img).save('diff'+str(N)+'.jpg')
    toimage(filtered_image).save('.\pics\outfile'+str(N)+'.jpg')
    plt.plot(errors)
    plt.show()
    #
    # plt.imshow(filtered_image)
    #
    # plt.gray()
    #
    # plt.show()