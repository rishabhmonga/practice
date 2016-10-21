def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    if x < 10:
        return True
    if x % 10 == 0:
        return False
    if x < 100 and x % 11 == 0:
        return True
    if x < 1000 and ((x / 100) * 10 + x % 10) % 11 == 0:
        return True

    v = x % 10
    x /= 10
    while x - v > 0:
        v = v * 10 + x % 10
        x /= 10
    if v > x:
        v /= 10
    return True if v == x else False


if __name__ == '__main__':
    # print(isPalindrome(12345))
    print(isPalindrome(12321))
    print(isPalindrome(121))
    print(isPalindrome(1))
