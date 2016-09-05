class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majCountIndex = 0
        count = 1
        for i in range(0, len(nums)):
            if nums[majCountIndex] == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                majCountIndex = i
                count = 1
            i += 1
        countCheck = 0
        for i in range(0, len(nums)):
            if nums[majCountIndex] == nums[i]:
                countCheck += 1
            if countCheck >= len(nums) / 2:
                return nums[majCountIndex]
            i += 1
        return -1

result = Solution()
print(result.majorityElement([3, 2, 3]))
