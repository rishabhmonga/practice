def merge(nums1, nums2):
    merged_list = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_list.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            merged_list.append(nums2[j])
            j += 1
        else:
            merged_list.append(nums1[i])
            merged_list.append(nums2[j])
            i += 1
            j += 1
    while i < len(nums1):
        merged_list.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged_list.append(nums2[j])
        j += 1
    return merged_list


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged_list = merge(nums1, nums2)
    result = 0.0
    if len(merged_list) % 2 == 0:
        result = merged_list[int(len(merged_list) / 2) - 1] + merged_list[int(len(merged_list) / 2)]
        result /= 2.0
    else:
        result = merged_list[int(len(merged_list) / 2)]
    return result


if __name__ == '__main__':
    # nums1 = [1, 2]
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    # nums2 = [3, 4]
    nums2 = [0, 6]
    print(merge(nums1, nums2))
    print(findMedianSortedArrays(nums1, nums2))
