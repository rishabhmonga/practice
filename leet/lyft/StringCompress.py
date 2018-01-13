def compress(s):
    if len(s) == 0:
        return s
    res = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            count += 1
        else:
            if count > 1:
                res += str(count)
            count = 1
            res += s[i]
    if count > 1:
        res += str(count)
    return res


if __name__ == '__main__':
    s = 'abbccc'
    # s = 'a'
    print(compress(s))

