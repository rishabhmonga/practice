class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ifRobbedPrevious = 0
        ifDidntRobPrevious = 0

        for i in range(0, len(nums)):
            currRobbed = ifDidntRobPrevious + nums[i]

            currNotRobbed = max(ifDidntRobPrevious, ifRobbedPrevious)

            ifDidntRobPrevious = currNotRobbed
            ifRobbedPrevious = currRobbed

        return max(ifRobbedPrevious, ifDidntRobPrevious)

soln = Solution()
print(soln.rob([1, 2, 3, 4, 5]))
print(soln.rob([2, 1, 1, 2]))
