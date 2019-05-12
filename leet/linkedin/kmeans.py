from random import shuffle, uniform

import math


def get_data(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    f.close()

    items = []

    for i in range(1, len(lines)):
        line = lines[i].split(',')
        itemFeatures = []

        for j in range(len(line) - 1):
            v = float(line
                      [j])
            itemFeatures.append(v)

        items.append(itemFeatures)

    shuffle(items)

    return items


def findColMinMax(items):
    mins = []
    maxs = []
    for row in items:
        mins.append(min(row))
        maxs.append(max(row))
    return mins, maxs


def initializeMeans(items, k, colMin, colMax):
    f = len(items[0])
    means = [[0 for _ in range(f)] for _ in range(k)]

    for m in means:
        for i in range(len(m)):
            m[i] = uniform(colMin[i] + 1, colMax[i] - 1)

    return means


def euclideanDistance(x, y):
    S = 0
    for i in range(len(x)):
        S += math.pow(x[i] - y[i], 2)

    return math.sqrt(S)


def update_mean(n, mean, item):
    for i in range(len(mean)):
        m = mean[i]
        m = (m * (n - 1) + item[i]) / float(n)
        mean[i] = round(m, 3)

    return mean


if __name__ == '__main__':
    data_points = get_data('data_kmeans.txt')
    print(data_points)
    minima, maxima = findColMinMax(data_points)
    print(minima)
    print(maxima)
    means = initializeMeans(data_points, 4, minima, maxima)

    print(means)

    updated_means = update_mean()
