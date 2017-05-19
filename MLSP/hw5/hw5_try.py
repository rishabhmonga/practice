import numpy as np
from collections import Counter
import math
from random import randint


def fastest_calc_dist(p1, p2):
    return math.sqrt((p2 - p1) ** 2)


def get_label(idx, idy, label_map, depth_map, disparity_matrix, clazz):
    lab_count = Counter()
    if idx > 0 and idy > 0:
        lab_count[label_map[idx - 1][idy - 1]] += 1
    if idx > 0:
        lab_count[label_map[idx - 1][idy]] += 1
        if idy < len(label_map[0])-1:
            lab_count[label_map[idx - 1][idy + 1]] += 1
    if idy > 0:
        lab_count[label_map[idx][idy - 1]] += 1
        if idy < len(label_map)-1:
            lab_count[label_map[idx + 1][idy - 1]] += 1

    if idy < len(label_map[0])-1:
        lab_count[label_map[idx][idy + 1]] += 1
    if idx < len(label_map[0])-1:
        lab_count[label_map[idx][idy + 1]] += 1
        lab_count[label_map[idx + 1][idy + 1]] += 1

    n_prob = []

    for i, j in lab_count.items():
        n_prob[i] = j / 8.0

    inv_dist = []
    for i in xrange(len(clazz)):
        inv_dist[i] = 1/fastest_calc_dist(disparity_matrix[idx][idy], clazz[i])
    sum_dist = sum(inv_dist)

    post_probs = []

    for i in xrange(len(inv_dist)):
        post_probs[i] = inv_dist[i]/sum_dist

    n_prob = np.array(n_prob)
    post_probs = np.array(post_probs)

    prob = np.multiply(n_prob, post_probs)
    return np.argmax(prob)


if __name__ == '__main__':
    test_arr = np.zeros((2, 2))
    print test_arr
    count = Counter()
    count[1] += 12
    count[2] += 50
    count[3] += 45

    n_prob = {}

    denominator =  float(sum(count.values()))

    for i, j in count.items():
        n_prob[i] = j / denominator

    print n_prob

    print randint(0, 5)


# def icm(label_map, depth_map, labels):
#     for i in range(len(label_map)):
#         for j in range(len(label_map[0])):
