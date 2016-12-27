class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000

        result = d[s[-1]]

        for i in range(len(s) -2, -1, -1):
            if d[s[i]] < d[s[i+1]]:
                result -= d[s[i]]
            else:
                result += d[s[i]]
        return result


soln = Solution()
print(soln.romanToInt('MCMXCVI'))

