def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    result = ''
    t = []
    i = 0
    while i <= len(s):
        if i < len(s) and s[i] is not ' ':
            t.append(s[i])
        else:
            while t:
                result += t.pop()
            result += ' '
        i += 1
    return result


if __name__ == '__main__':
    print(reverseWords("Let's take LeetCode contest"))
    # print(reverseWords("Let's"))
