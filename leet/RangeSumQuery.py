class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(1, len(self.nums)):
            nums[i] += nums[i-1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i-1]


if __name__ == '__main__':
    arr = NumArray([-2, 0, 3, -5, 2, -1])
    print(arr.sumRange(0, 2))
