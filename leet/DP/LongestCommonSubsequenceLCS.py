def LCS(s1, s2):
    dp_table = [[0]*(len(s2)+1)]*(len(s1)+1)
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1] + 1
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])
    return dp_table[len(s1)][len(s2)]

if __name__ == '__main__':
    print LCS('AGGTAB', 'GXTXAYB')
