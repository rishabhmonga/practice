def merge_arrays(l_arr, r_arr):
    result = []
    l_idx = 0
    r_idx = 0
    while l_idx < len(l_arr) and r_idx < len(r_arr):
        if l_arr[l_idx] < r_arr[r_idx]:
            result.append(l_arr[l_idx])
            l_idx += 1
        else:
            result.append(r_arr[r_idx])
            r_idx += 1
    while l_idx < len(l_arr):
        result.append(l_arr[l_idx])
        l_idx += 1
    while r_idx < len(r_arr):
        result.append(r_arr[r_idx])
        r_idx += 1
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge_arrays(left, right)


if __name__ == '__main__':
    arr = [856,43,231,47,9,2,467,3]
    print merge_sort(arr)
    l_arr = [1, 3, 5, 8]
    r_arr = [2, 4, 6]
    print merge_arrays(l_arr, r_arr)
