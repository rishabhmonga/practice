class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num is 1:
            return True
        elif num is 0:
            return False
        if num % 2 is 0:
            return self.isUgly(num / 2)
        elif num % 3 is 0:
            return self.isUgly(num / 3)
        elif num % 5 is 0:
            return self.isUgly(num / 5)
        return False
soln = Solution()
print(soln.isUgly(6))
print(soln.isUgly(1))
print(soln.isUgly(8))
print(soln.isUgly(14))
