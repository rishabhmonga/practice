def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    res = []
    for i in range(left, right + 1):
        if selfDivision(i):
            res.append(i)
    return res


def selfDivision(x):
    copy = x
    while copy > 0:
        dig = copy % 10
        if dig == 0:
            return False
        if x % dig != 0:
            return False
        copy = copy // 10
    return True


if __name__ == '__main__':
    left = 1
    right = 22

    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    print(selfDividingNumbers(left, right))
