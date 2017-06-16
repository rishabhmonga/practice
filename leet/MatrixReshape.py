def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if r * c != len(nums) * len(nums[0]):
        return nums
    result = [[_ for _ in range(c)] for _ in range(r)]
    idx = idy = 0
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if idy == c:
                idy = 0
                idx += 1
            result[idx][idy] = nums[i][j]
            idy += 1

    return result


if __name__ == '__main__':
    print(matrixReshape([[1, 2], [3, 4]], 1, 4))
    print(matrixReshape([[1, 2], [3, 4]], 2, 4))
