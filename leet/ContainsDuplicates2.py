def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    num_set = set()
    if len(nums) == 0:
        return False
    for i in range(len(nums)):
        if i > k:
            num_set.remove(nums[i-k-1])
        if nums[i] not in num_set:
            num_set.add(nums[i])
        else:
            return True
    return False


if __name__ == '__main__':
    print(containsNearbyDuplicate([-1, -1], 1))
