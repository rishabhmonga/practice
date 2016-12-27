import sys


def myAtoi(num_str):
    """
    :type num_str: str
    :rtype: int
    """
    try:
        if len(num_str) == 0:
            return 0
        alpha_idx = 0
        num_str = num_str.lstrip()
        idx = 0
        if num_str[0] is '-' or num_str is '+':
            idx += 1
        for i in range(idx, len(num_str)):
            if num_str[i].isdigit():
                continue
            else:
                alpha_idx = i
                break
        if alpha_idx != 0:
            num_str = num_str[0:alpha_idx]
        num = int(num_str)
        if num < -2147483648:
            return -2147483648
        elif num > 2147483647:
            return 2147483647
        else:
            return num
    except ValueError:
        return 0

if __name__ == '__main__':
    # print(myAtoi('123 456'))
    print(myAtoi("  -0012a42"))

