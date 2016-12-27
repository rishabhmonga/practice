def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    if len(s) == 0:
        return True
    s_mask = get_char_mask(s)
    t_mask = get_char_mask(t)
    return True if s_mask == t_mask else False


def get_char_mask(str1):
    mask = []
    count = 1
    prev = str1[0]
    for i in range(1, len(str1)):
        curr = str1[i]
        if curr == prev:
            count += 1
        else:
            mask.append(count)
            count = 1
        prev = curr
    mask.append(count)
    return mask


if __name__ == '__main__':
    print(isIsomorphic("hello", 'world'))
    print(isIsomorphic("aa", 'bb'))
    print(isIsomorphic("apple", 'elppa'))
    print(isIsomorphic('aba', 'baa'))
