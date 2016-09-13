class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and ((n & n-1) == 0)

soln = Solution()
print(soln.isPowerOfTwo(46))
print(soln.isPowerOfTwo(64))
print(soln.isPowerOfTwo(128))
print(soln.isPowerOfTwo(1))
print(soln.isPowerOfTwo(0))
