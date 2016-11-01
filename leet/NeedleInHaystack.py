def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(haystack) < len(needle):
        return -1
    elif len(needle) == 0:
        return 0
    i = 0
    idx = -1
    for j in range(len(haystack)):
        if needle[i] == haystack[j]:
            if i == 0 and idx == -1:
                idx = j
            i += 1
        else:
            i = 0
            idx = -1
        if i == len(needle):
            return idx
    return -1


if __name__ == '__main__':
    # print(strStr('a', ''))
    # print(strStr('', 'a'))
    # print(strStr('aaa', 'aaaa'))
    print(strStr("mississippi", "issip"))

