class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp_table = [0 for _ in range(len(s)+1)]
        dp_table[len(s)] = 1
        dp_table[len(s) - 1] = 1 if s[len(s) - 1] != '0' else 0

        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                continue
            else:
                if int(s[i:i+2]) <= 26:
                    dp_table[i] = dp_table[i+1] + dp_table[i+2]
                else:
                    dp_table[i] = dp_table[i+1]
        print("DP Table : ", dp_table)
        return dp_table[0]


if __name__ == '__main__':
    ans = Solution()
    print(ans.numDecodings('26'))
