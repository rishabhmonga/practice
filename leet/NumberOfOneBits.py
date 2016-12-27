class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        numberOfOneBits = 0
        while n > 0:
            if n % 2 != 0:
                numberOfOneBits += 1
            n >>= 1
        return numberOfOneBits

soln = Solution()
print(soln.hammingWeight(4))
print(soln.hammingWeight(2147483648))
