def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    try:
        return int(str)
    except ValueError:
        return 0

if __name__ == '__main__':
    print(myAtoi('ab'))

