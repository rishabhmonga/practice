def three_sum_zero(nums):
    ans = set()
    nums = sorted(nums)
    n = len(nums)

    for i in nums:
        target_sum = 0 - i
        x = 0
        y = n - 1
        while x < y:
            if nums[x] + nums[y] == target_sum:
                ans.add(tuple(sorted([i, nums[x], nums[y]])))
                x += 1
                y -= 1
            elif nums[x] + nums[y] > target_sum:
                y -= 1
            else:
                x += 1
    return ans


if __name__ == '__main__':
    nums = [-5, 1, 10, 2, 3]
    print(three_sum_zero(nums))