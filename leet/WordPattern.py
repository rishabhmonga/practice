def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    if pattern == '' and str == '':
        return True
    input_str = str.split(' ')
    if len(input_str) != len(pattern):
        return False
    word_idx = {}
    for i in range(len(input_str)):
        if pattern[i] not in word_idx and input_str[i] not in word_idx.values():
            word_idx[pattern[i]] = input_str[i]
        elif pattern[i] not in word_idx or word_idx[pattern[i]] != input_str[i]:
            return False
    return True

if __name__ == '__main__':
    # wordPattern("abba", "dog cat cat dog")
    print(wordPattern("abba", "dog dog dog dog"))
