def encoding(s):
    for c in s:
        print(c, ord(c))


def __DecimalToAnyBaseArrayRecur__(array, decimal, base):
    array.append(decimal % base)
    div = decimal // base
    if div == 0:
        return
    __DecimalToAnyBaseArrayRecur__(array, div, base)


def DecimalToAnyBaseArray(decimal, base):
    array = []
    if base < 2 or not str(base).isdigit():
        print('incorrect base value')
        exit(1)
    __DecimalToAnyBaseArrayRecur__(array, decimal, base)
    return arr2int(array[::-1])


def __AnyBaseArrayToDecimalRecur__(array, decimal, base=10):
    array.append(decimal % base)
    div = decimal // base
    if div == 0:
        return
    __DecimalToAnyBaseArrayRecur__(array, div, base)


def AnyBaseArrayToDecimaArray(decimal):
    base = 10

    array = []
    if base < 2 or not str(base).isdigit():
        print('incorrect base value')
        exit(1)
    __AnyBaseArrayToDecimalRecur__(array, decimal, 10)
    return arr2int(array[::-1])


def arr2int(arr):
    count = 0
    res = 0
    for i in reversed(arr):
        res += i * 10 ** count
        count += 1
    return res


def converter(number, base):
    # split number in figures
    figures = [int(i) for i in str(number)]
    # invert oder of figures (lowest count first)
    figures = figures[::-1]
    result = 0
    # loop over all figures
    for i in range(len(figures)):
        # add the contirbution of the i-th figure
        result += figures[i] * base ** i
        print(figures[i])
    return result


if __name__ == '__main__':
    # s = 'hello'
    # encoding(s)
    # res = DecimalToAnyBaseArray(14, 6)
    # print(res)
    # res = AnyBaseArrayToDecimaArray(int(res))
    # print(res)
    print(converter(45, 22))
