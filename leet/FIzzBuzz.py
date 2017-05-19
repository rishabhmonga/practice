def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = list()
    for i in range(1, n + 1):
        str_result = ''
        if i % 3 == 0:
            str_result += 'Fizz'
        if i % 5 == 0:
            str_result += 'Buzz'
        if str_result == '':
            str_result = str(i)
        result.append(str_result)
    return result


if __name__ == '__main__':
    print fizzBuzz(15)
