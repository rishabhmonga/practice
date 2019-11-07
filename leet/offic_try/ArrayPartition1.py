def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = []
    nums = sorted(nums)
    for itr in range(0, len(nums), 2):
         res.append(nums[itr])
    return res

if __name__ == '__main__':
    x = [1, 4, 3, 2]
    print(arrayPairSum(x))
