def findPivot(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = int(start + (end - start) / 2)
        if arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = mid
    return start


def binarySearch(arr, x):
    if arr is None or len(arr) == 0:
        return -1

    pivot = findPivot(arr)
    if x == arr[pivot]:
        return pivot

    start = 0
    if x <= arr[-1]:
        start = pivot

    end = len(arr) - 1
    if x > arr[-1]:
        end = pivot

    while start <= end:
        mid = int(start + (end - start) / 2)
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 1, 2, 3, 4]
    print(binarySearch(arr, 7))
