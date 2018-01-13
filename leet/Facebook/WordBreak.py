def wordBreak(s, dictionary):
    m = len(s)
    dp_table = [False] * (m + 1)
    dp_table[0] = True
    for i in range(1, m + 1):
        for j in range(i):
            if dp_table[j] and s[j:i] in dictionary:
                dp_table[i] = True
                break
    print(dp_table)
    return dp_table[m]


def wordBreak2(s, wordDict):
    memo = {len(s): ['']}

    def sentences(i):
        if i not in memo:
            memo[i] = [s[i:j] + (tail and ' ' + tail) for j in range(i + 1, len(s) + 1) if s[i:j] in wordDict for tail in sentences(j)]
        return memo[i]

    return sentences(0)


if __name__ == '__main__':
    s = 'leetcode'
    dictionary = ['leet', 'code']
    print(wordBreak(s, dictionary))
    print(wordBreak2(s, dictionary))
