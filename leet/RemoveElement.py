class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            if val in nums:
                nums.remove(val)
        return len(nums)

soln = Solution()
print(soln.removeElement([3, 3], 3))
