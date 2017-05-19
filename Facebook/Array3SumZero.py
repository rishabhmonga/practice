def threeSum(nums):
    nums.sort()
    res = []
    for i in xrange(len(nums)):
        if i != 0 and nums[i] == nums[i - 1]: continue
        target = -nums[i]
        l, r = i + 1, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]: l += 1
                while l < r and nums[r] == nums[r - 1]: r -= 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return res


if __name__ == '__main__':
    S = [-1, 0, 1, 2, -1, -4]
    S = [0, 0, 0, 0]
    # S = [3, 0, -2, -1, 1, 2]
    print threeSum(S)
