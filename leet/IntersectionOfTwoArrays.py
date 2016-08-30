class IntersectionOfTwoArrays:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return set1.intersection(set2)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
intersect = IntersectionOfTwoArrays()
print(intersect.intersection(nums1, nums2))
