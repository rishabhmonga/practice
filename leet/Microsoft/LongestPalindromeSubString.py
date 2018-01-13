# def longestPalSubstr(string):
#     maxLength = 1
#     dp_table = [[0 for _ in range(len(string))] for _ in range(len(string))]
#     i = 0
#     while i < len(string):
#         dp_table[i][i] = True
#         i += 1
#
#     start, i = 0, 0
#
#     # length = 2 substrings
#     while i < len(string) - 1:
#         i = 0
#
#
#     pass


def longestPalindrome(s):
    if len(s) == 0:
        return 0
    maxLen = 1
    start = 0
    for i in range(len(s)):
        if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
            start = i - maxLen - 1
            maxLen += 2
            continue

        if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
            start = i - maxLen
            maxLen += 1
    return s[start:start + maxLen]


if __name__ == '__main__':
    string = "forgeeksskeegfor"
    string = "aab"
    print("Length is: " + str(longestPalindrome(string)))
