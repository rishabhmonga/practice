def isBadVersion(version):
    """
    :param version: int
    :return: bool
    """
    return False if version < 2 else True


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    if isBadVersion(n) is True and isBadVersion(n - 1) is False:
        return n
    isBad = isBadVersion(n)
    if isBad is True:
        return int(firstBadVersion(n / 2))
    elif isBad is False:
        return int(firstBadVersion(3 * n / 2))

    """
    r = n-1
    l = 0
    while(l<=r):
        mid = l + (r-l)/2
        if isBadVersion(mid)==False:
            l = mid+1
        else:
            r = mid-1
    return l
    """


if __name__ == '__main__':
    print(firstBadVersion(3))
