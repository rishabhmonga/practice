def array_sum(arr, x):
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[i] + arr[j] == x:
            return (arr[i], arr[j])
        elif arr[i] + arr[j] < x:
            i += 1
        else:
            j -= 1
    return 0


if __name__ == '__main__':
    arr = [12,23,43,5,6,2,11,45]
    print sorted(arr)
    print array_sum(sorted(arr), 54)
