class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0

soln = Solution()
print(soln.isPowerOfThree(243))
print(soln.isPowerOfThree(21))
print(soln.isPowerOfThree(27))
print(soln.isPowerOfThree(1))
