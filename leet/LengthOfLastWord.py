def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s_list = s.split(' ')
    print(s_list)
    if s_list[-1] is '' and len(s_list) > 1:
        return len(s_list[-2])
    return len(s_list[-1]) if len(s_list) > 0 else 0

if __name__ == '__main__':
    print(lengthOfLastWord("a "))
