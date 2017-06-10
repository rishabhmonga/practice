def move_zeros(arr):
    zero_start = 0
    i = 0
    while i < len(arr):
        if arr[i] != 0:
            if arr[zero_start] == 0:
                # swap
                temp = arr[i]
                arr[i] = arr[zero_start]
                arr[zero_start] = temp
            else:
                zero_start += 1
        i += 1
    return arr

def moveZeroes(nums):
    zeroStart = 0
    runner = 0
    while runner < len(nums):
        if nums[runner] is not 0:
            if nums[zeroStart] is 0:
                # swap
                temp = nums[runner]
                nums[runner] = nums[zeroStart]
                nums[zeroStart] = temp
            if nums[zeroStart] is not 0:
                zeroStart += 1
        runner += 1
    print(nums)

if __name__ == '__main__':
    arr1 = [1, 0, 2, 3, 0, 4, 0, 0, 5]

    print moveZeroes(arr1)
    print move_zeros(arr1)
