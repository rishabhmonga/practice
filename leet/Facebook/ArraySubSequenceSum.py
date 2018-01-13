def check_sum(nums, target_sum):
    ans = set()
    nums = sorted(nums)
    n = len(nums)
    for x in nums:
        goal = target_sum - x
        i = 0
        j = n - 1
        while j > i:
            if nums[i] + nums[j] == goal:
                ans.add(tuple(sorted([x, nums[i], nums[j]])))
                i += 1
                j -= 1
            elif nums[i] + nums[j] > goal:
                j -= 1
            else:
                i += 1
    print(ans)
    return True if len(ans) else False


def check_sequence_sum(nums, goal):
    i = 0
    start = 0
    curr_sum = 0
    n = len(nums)
    while i < n:
        if curr_sum + nums[i] < goal:
            curr_sum += nums[i]
        elif curr_sum + nums[i] == goal:
            return True
        else:
            curr_sum += nums[i]
            while curr_sum > goal:
                curr_sum -= nums[start]
                start += 1
            if curr_sum == goal:
                return True
        i += 1
    return False


if __name__ == '__main__':
    print(check_sequence_sum([23, 5, 4, 7, 2, 11], 20))
    print(check_sequence_sum([1, 3, 5, 23, 2], 8))
    print(check_sequence_sum([1, 3, 5, 23, 2], 7))
