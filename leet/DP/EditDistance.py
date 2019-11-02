def edit_distance(s1, s2):
    dp_table = [[0] * (len(s2) + 1)] * (len(s1) + 1)
    # print(dp_table)

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                dp_table[i][j] = j
            elif j == 0:
                dp_table[i][j] = i

            elif s1[i - 1] == s2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1]

            else:
                dp_table[i][j] = 1 + min(dp_table[i - 1][j],
                                         dp_table[i][j - 1],
                                         dp_table[i - 1][j - 1]
                                         )
    print(dp_table)
    return dp_table[len(s1)][len(s2)]


def isOneEditDistance(s, t):
    if s == t:
        return False
    l1, l2 = len(s), len(t)
    if l1 > l2:  # force s no longer than t
        return isOneEditDistance(t, s)
    if l2 - l1 > 1:
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            if l1 == l2:
                s = s[:i] + t[i] + s[i + 1:]  # replacement
            else:
                s = s[:i] + t[i] + s[i:]  # insertion
            break
    return s == t or s == t[:-1]  # checking edge case for s ="a", t = ""


if __name__ == '__main__':
    print(edit_distance('geek', 'gesek'))
    print(isOneEditDistance('geek', 'gesek'))
    s = 'geek'
