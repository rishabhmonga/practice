class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        listElements = set()
        for i in nums:
            if i not in listElements:
                listElements.add(i)
            else:
                return True
        return False


result = Solution()
print(result.containsDuplicate([3, 2, 3]))
print(result.containsDuplicate([1, 2, 3]))
