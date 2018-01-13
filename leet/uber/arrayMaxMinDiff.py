import math


def findDiff(arr):
    if arr is None or len(arr) == 0:
        return -1
    start, end = 0, len(arr) - 1
    min = max = 0
    while start < len(arr) or end > 0:
        if start < len(arr) and arr[start] < arr[min]:
            min = start
        start += 1
        if end > 0 and arr[end] > arr[max]:
            max = end
        end -= 1
        print(min, max)
    return (arr[min], arr[max])


arr = [34, 46, 1, 57, 4, 24]
print(findDiff(arr))
