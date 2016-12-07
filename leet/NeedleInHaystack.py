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
    for j in range(0, len(haystack) - len(needle) + 1):
        i = 0
        while i < len(needle):
            if needle[i] != haystack[j + i]:
                break
            i += 1
        if i == len(needle):
            return j
    return -1


if __name__ == '__main__':
    print(strStr('a', 'a'))
    print(strStr('a', ''))
    print(strStr('', 'a'))
    print(strStr('aaa', 'aaaa'))
    print(strStr("mississippi", "issip"))
    print(strStr("mississippi", "issipi"))

