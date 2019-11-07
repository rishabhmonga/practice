def qs_sort(nums):
    pivot = nums[-1]
    i = 0
    j = len(nums) - 2
    while i < j:
        if nums[i] > pivot:
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    nums[i], nums[-1] = nums[-1], nums[i]

    return nums



def qs(nums):
    qs_sort(nums)
    return nums


if __name__ == '__main__':
    arr = [23, 453, 7, 12, 3, 65, 19]
    print(qs_sort(arr))
