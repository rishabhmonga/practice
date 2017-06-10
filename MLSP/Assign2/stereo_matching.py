import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random
# import k_means
import math
import seaborn as sns


def get_disparity_matrix(left_image, right_image):
    lengthL, widthL, heightL = left_image.shape
    lengthR, widthR, heightR = right_image.shape

    window_size = 40
    disparity_matrix = np.zeros((left_image.shape[0], left_image.shape[1] - window_size))
    for i in range(lengthR):
        for j in range(widthR - window_size):
            temp = []
            for k in range(j, j + window_size):
                temp.append(np.linalg.norm(right_image[i][j] - left_image[i][k]))
            disparity_matrix[i][j] = np.min(temp)
    return disparity_matrix


def get_means(disparity_matrix):
    k = 3
    centroids = np.empty(k)
    centroids[0] = disparity_matrix[0][1]
    centroids[1] = disparity_matrix[25][36]
    centroids[2] = disparity_matrix[300][300]

    aa = np.empty(k)
    cl = np.empty((disparity_matrix.shape[0], disparity_matrix.shape[1]))
    for i in range(disparity_matrix.shape[0]):
        for j in range(disparity_matrix.shape[1]):
            for ij in range(k):
                aa[ij] = np.sqrt(np.sum((disparity_matrix[i][j] - centroids[ij]) ** 2))
            cl[i][j] = np.argmin(aa)
    print(cl.shape)

    sum1 = sum2 = sum3 = c1 = c2 = c3 = 0
    for i in range(disparity_matrix.shape[0]):
        for j in range(disparity_matrix.shape[1]):
            if cl[i][j] == 0:
                sum1 += disparity_matrix[i][j]
                c1 += 1
            elif cl[i][j] == 1:
                sum2 += disparity_matrix[i][j]
                c2 += 1
            else:
                sum3 += disparity_matrix[i][j]
                c3 += 1
    avg1 = (sum1 / c1)
    avg2 = (sum2 / c2)
    avg3 = (sum3 / c3)

    for i in range(disparity_matrix.shape[0]):
        for j in range(disparity_matrix.shape[1]):
            if cl[i][j] == 0:
                disparity_matrix[i][j] = avg1
            elif cl[i][j] == 1:
                disparity_matrix[i][j] = avg2
            else:
                disparity_matrix[i][j] = avg3
    print(disparity_matrix.shape)

    return disparity_matrix, avg1, avg2, avg3


if __name__ == '__main__':
    im0 = Image.open('im0.ppm')
    im8 = Image.open('im8.ppm')
    left_image = np.asarray(im0, dtype="int32")
    right_image = np.asarray(im8, dtype="int32")

    disparity_matrix = get_disparity_matrix(left_image, right_image)
    a = np.copy(disparity_matrix)

    vectorized = np.ndarray.flatten(disparity_matrix)
    plt.hist(vectorized)
    plt.show()

    sns.set_style("whitegrid", {'axes.grid': False})
    cmap = sns.diverging_palette(145, 280, s=85, l=25, n=7, as_cmap=True)
    plt.imshow(disparity_matrix, cmap=cmap)
    plt.show()

    depth_map, mean1, mean2, mean3 = get_means(a)

    cmap = sns.cubehelix_palette(start=2.8, rot=4.7, as_cmap=True)
    plt.imshow(depth_map, cmap)
    plt.show()
