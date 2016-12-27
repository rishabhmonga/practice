def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) <= 1:
        return []
    result = {}
    for i in range(len(nums)):
        if nums[i] in result:
            return [result[nums[i]], i]
        else:
            result[target - nums[i]] = i

if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))