def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    i, j = 0, 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums1[i]:
            j += 1
        else:
            result.append(nums2[j])
            j += 1
            i += 1
    return result


if __name__ == '__main__':

    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [1, 2, 2, 1]
    nums2 = [2]
    print(intersection(nums1, nums2))
