class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i, j in reversed(list(enumerate(digits))):
            if j < 9:
                digits[i] += 1
                return digits
            elif i is 0 and j == 9:
                digits[i] = 0
                digits.insert(0, 1)
                return digits
            else:
                digits[i] = 0
        return digits


soln = Solution()
print(soln.plusOne([1, 2, 3]))
print(soln.plusOne([9, 9, 9]))
