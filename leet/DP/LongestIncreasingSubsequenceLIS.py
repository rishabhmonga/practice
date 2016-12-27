def LIS(arr):
    LS = [1]*len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and LS[i] < LS[j] + 1:
                LS[i] = LS[j] + 1
    return max(LS)


if __name__ == '__main__':
    print LIS([10, 22, 9, 33, 21, 50, 41, 60])