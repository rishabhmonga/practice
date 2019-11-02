import random


def selectKItems(stream, n, k):
    reservoir = stream[:5]

    i = k + 1
    while i < n:
        j = random.randrange(len(reservoir))
        if j < k:
            reservoir[j] = stream[i]
        i += 1
    print(reservoir)


if __name__ == '__main__':
    stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(stream)
    k = 5
    selectKItems(stream, n, k)
