class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f1 = 2
        f2 = 1
        if n is 1:
            return f2
        elif n is 2:
            return f1
        fn = 0
        for i in range(3, n+1):
            fn = f1 + f2
            f2 = f1
            f1 = fn
        return fn


soln = Solution()
print(soln.climbStairs(4))
print(soln.climbStairs(5))
print(soln.climbStairs(1))
print(soln.climbStairs(44))
