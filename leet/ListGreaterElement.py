def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    for i in range(len(findNums)):
        curr = findNums[i]
        flag = False
        idx = -1
        for j in range(len(nums)):
            if findNums[i] == nums[j]:
                flag = True
                continue
            if flag:
                if curr < nums[j]:
                    idx = nums[j]

                    break
        result.append(idx)
    return result


if __name__ == '__main__':
    # print(nextGreaterElement([2, 4], [1, 2, 3, 4]))

    # [-1, 3, -1]
    # print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))

    # [-1,-1,-1,-1,-1]
    print(nextGreaterElement([1, 3, 5, 2, 4], [5, 4, 3, 2, 1]))
