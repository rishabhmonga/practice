def binary_search(nums, x):
    if nums is None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        if nums[0] == x:
            return nums[0]
        else:
            return -1
    idx_mid = int(len(nums) / 2)
    mid = nums[idx_mid]
    if mid == x:
        return mid
    if mid < x:
        return binary_search(nums[idx_mid+1:len(nums)], x)
    if mid > x:
        return binary_search(nums[0:idx_mid], x)


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], -1))
