def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # for _ in range(k):
    #     temp = nums[-1]
    #     nums.remove(nums[-1])
    #     nums.insert(0, temp)
    n = len(nums)
    k = k % n
    nums[:] = nums[n - k:] + nums[:n - k]


if __name__ == '__main__':
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = [1, 2]
    rotate(num, 4)
    rotate(num, 3)
    print(num)
