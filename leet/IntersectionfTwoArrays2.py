class IntersectionOfTwoArrays:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [val for val in nums1 if val in nums2]
        # return list(set(nums1).intersection(set(nums2)))

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
# nums1 = [1, 2, 2, 1]
# nums2 = [2]
intersect = IntersectionOfTwoArrays()
print(intersect.intersection(nums1, nums2))
