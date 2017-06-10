def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    row1 = 'qwertyuiop'
    row2 = 'asdfghjkl'
    row3 = 'zxcvbnm'
    result = []
    print set(words[1]).union(row1)
    for word in words:
        if len(set(word).union(row1)) == len(row1) or len(set(word).union(row2)) == len(row2) or len(set(word).union(row3)) == len(row3) :
            result.append(word)

    return result

if __name__ == '__main__':
    print findWords(["Hello","Alaska","Dad","Peace"])
