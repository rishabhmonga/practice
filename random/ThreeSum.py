def threeSum(nums, sum):
    soln = set()
    nums = sorted(nums)
    size = len(nums)

    for i in nums:
        target_sum = sum - i
        x = 0
        y = size - 1
        while x < y:
            if nums[x] + nums[y] == target_sum:
                soln.add(tuple(sorted([i, nums[x], nums[y]])))
                x += 1
                y -= 1
            elif nums[x] + nums[y] > target_sum:
                y -= 1
            else:
                x += 1

    return soln


if __name__ == '__main__':
    nums = [3, 35, 2, 5, 7, 12]
    print(threeSum(nums, 10))
