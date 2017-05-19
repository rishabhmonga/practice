from random import randint


def shuffle(arr):
    indexes = reversed(range(len(arr)))

    def swap(arr, idx1, idx2):
        temp = arr[idx1]
        arr[idx1] = arr[idx2]
        arr[idx2] = temp

    for i in indexes:
        swap(arr, i, randint(0, i))
    return arr


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print shuffle(arr=arr1)
