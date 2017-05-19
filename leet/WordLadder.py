def ladderLength(beginWord, endWord, wordDict):
    length = 2
    front, back = {beginWord}, {endWord}
    wordDict.discard(beginWord)
    while front:
        # generate all valid transformations
        front = wordDict & (set(word[:index] + ch + word[index + 1:] for word in front
                                for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
        if front & back:
            # there are common elements in front and back, done
            return length
        length += 1
        if len(front) > len(back):
            # swap front and back for better performance (fewer choices in generating nextSet)
            front, back = back, front
        # remove transformations from wordDict to avoid cycle
        wordDict -= front
    return 0


def ladderLength2(beginWord, endWord, wordDict):
    """
    :type beginWord: str
    :type endWord: str
    :type wordDict: Set[str]
    :rtype: int
    """

    def generateNextSet1(current, wordDict, wordLen):
        nextSet = set()
        for word in current:
            for index in range(wordLen):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:index] + ch + word[index + 1:]
                    if nextWord in wordDict:
                        nextSet.add(nextWord)
        return nextSet

    def generateNextSet2(current, wordDict):
        nextSet = set()
        for word in current:
            for nextWord in wordDict:
                index = 0
                try:
                    while word[index] == nextWord[index]:
                        index += 1
                    if word[index + 1:] == nextWord[index + 1:]:
                        nextSet.add(nextWord)
                except:
                    continue
        return nextSet

    steps, wordLen = 2, len(beginWord)
    front, back = {beginWord}, {endWord}
    wordDict.discard(beginWord)
    switchThreshold = 26 * wordLen
    while front:
        # get all valid transformations
        if len(wordDict) >= switchThreshold:
            front = generateNextSet1(front, wordDict, wordLen)
        else:
            front = generateNextSet2(front, wordDict)
        if front & back:
            # there are common elements in front and back, done
            return steps
        steps += 1
        if len(front) >= len(back):
            # swap front and back for better performance (smaller nextSet)
            front, back = back, front
        # remove transformations from wordDict to avoid cycles
        if (len(wordDict) >> 1) >= len(front):
            # s.difference_update(t): O(len(t))
            wordDict -= front
        else:
            # s.difference(t): O(len(s))
            wordDict = wordDict - front
    return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = {"hot", "dot", "dog", "lot", "log"}
    print ladderLength(beginWord, endWord, wordList)
    print ladderLength2(beginWord, endWord, wordList)
