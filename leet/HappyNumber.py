class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = list()
        while n > 0:
            digits.append(n % 10)
            n = int(n / 10)
        sqSum = 0
        for i in digits:
            sqSum += i * i
        return sqSum == 1 or sqSum > 9 and self.isHappy(sqSum)


soln = Solution()
print(soln.isHappy(46))
print(soln.isHappy(19))
print(soln.isHappy(4))
