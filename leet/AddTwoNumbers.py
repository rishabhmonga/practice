class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # if b == 0:
        #     return a
        # add_result = a ^ b
        # carry = (a & b) << 1
        #
        # return Solution.getSum(self, add_result, carry)

        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

print(Solution().getSum(-1, 2))
