def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    result = ''
    chars = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    while n > 0:
        result = chars[(n - 1) % 26] + result
        n = (n - 1) // 26
    return result


if __name__ == '__main__':
    print(convertToTitle(2))
    for i in range(100):
        print(i, convertToTitle(i))
