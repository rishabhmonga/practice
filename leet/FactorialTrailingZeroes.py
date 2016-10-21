def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    return 0 if n == 0 else n / 5 + trailingZeroes(n / 5)

if __name__ == '__main__':
    print(trailingZeroes(100))
