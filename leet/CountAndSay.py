class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # corner case
        if n == 1:
            return '1'
        else:
            # recursion
            s = self.countAndSay(n-1)
            digit, count = s[0], 1
            res = ''
            for c in s[1:]:
                if c == digit:
                    count += 1
                # change of current digit
                else:
                    res += str(count) + str(digit)
                    digit, count = c, 1
            res += str(count) + str(digit)
            return res


if __name__ == '__main__':
    soln = Solution()
    print(soln.countAndSay(1))
    print(soln.countAndSay(2))
    print(soln.countAndSay(3))
