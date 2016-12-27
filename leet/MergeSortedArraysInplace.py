def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    j = 0
    i = 0
    while j < len(nums2):
        while i < len(nums1) and nums1[i] < nums2[j]:
            i += 1
        insert_digit(nums2[j], nums1, i)
        j += 1
        i += 1


def insert_digit(n, nums, i):
    if i < len(nums):
        temp = nums[-1]
        for a in range(i, len(nums) - 1):
            temp = nums[a + 1]
            nums[a + 1] = nums[a]
        nums.append(temp)
        nums[i] = n
    else:
        nums.append(n)


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 7]
    nums2 = [5, 6]
    print(nums1)
    print(nums2)
    print("merge")
    merge(nums1, len(nums1), nums2, len(nums2))
    print(nums1)
