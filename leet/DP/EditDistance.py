def edit_distance(s1, s2):
    dp_table = [[0] * (len(s2) + 1)] * (len(s1) + 1)
    print dp_table
    dp_table = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    print dp_table

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                dp_table[i][j] = j
            elif j == 0:
                dp_table[i][j] = i

            elif s1[i-1] == s2[j-1]:
                dp_table[i][j] = dp_table[i - 1][j - 1]

            else:
                dp_table[i][j] = 1 + min(dp_table[i - 1][j],
                                         dp_table[i][j - 1],
                                         dp_table[i - 1][j - 1]
                                         )
    print dp_table
    return dp_table[len(s1)][len(s2)]


if __name__ == '__main__':
    print edit_distance('geek', 'gesek')
