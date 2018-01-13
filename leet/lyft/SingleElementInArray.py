def __get_single__(nums, start, end):
    if start >= end:
        return -1

    while start < end:
        mid = start + (end - 1)//2

        if mid % 2 == 1:
            mid -= 1

        if nums[mid] != nums[mid + 1]:
            end = mid

        else:
            start = mid + 2

    return nums[start]


def find_single(nums):
    return __get_single__(nums, 0, len(nums) - 1)


def bin_search(nums, x, start, end):
    if start >= end:
        return -1
    mid = start + (end - 1) // 2

    if nums[mid] == x:
        return mid

    elif nums[mid] > x:
        return bin_search(nums, x, start, mid - 1)

    elif nums[mid] < x:
        return bin_search(nums, x, mid + 1, end)


def binary_search(nums, x):
    return bin_search(nums, x, 0, len(nums) - 1)


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 4))
    arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(find_single(arr))
