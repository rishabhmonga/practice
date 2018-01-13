def count(arr, x):
    low, high = 0, len(arr) - 1

    result = [-1, -1]

    while low < high:
        mid = int(low + (high - low) / 2)
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    if arr[low] != x:
        return result
    else:
        result[0] = low

    high = len(arr) - 1
    while low < high:
        mid = int(low + (high - low) / 2) + 1
        if arr[mid] > x:
            high = mid - 1
        else:
            low = mid

    result[1] = high

    return result


arr = [1, 2, 2, 3, 3, 3, 3]
x = 3

result = count(arr, 1)
print(result, result[1] - result[0] + 1)
