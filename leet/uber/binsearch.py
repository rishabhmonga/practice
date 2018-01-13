def bsearch(arr, x, low, high):
    mid = int((low + high) / 2)
    if low <= high:
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bsearch(arr, x, low, mid - 1)
        else:
            return bsearch(arr, x, mid, high)
    else:
        return -1


def binsearch(arr, x):
    if arr is None or x is None or not len(arr):
        return -1
    return bsearch(arr, x, 0, len(arr))


def bSearchIt(arr, x):
    if arr is None or x is None or not len(arr):
        return -1
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [2, 3, 4, 10, 40]
x = 1
# result = binsearch(arr, x)
print(bSearchIt(arr, x))
