def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums[0]
    from sys import maxsize
    first_max = second_max = third_max = -maxsize
    visited = set()
    for i in nums:
        if i > first_max:
            third_max = second_max
            second_max = first_max
            first_max = i
            visited.add(i)
        elif i > second_max and i not in visited:
            third_max = second_max
            second_max = i
            visited.add(i)
        elif i > third_max and i not in visited:
            third_max = i
            visited.add(i)

    return third_max if third_max > -maxsize else first_max


if __name__ == '__main__':
    print(thirdMax([3, 1, 2]))
    print(thirdMax([1, 2]))
    print(thirdMax([2, 2, 3, 1]))
