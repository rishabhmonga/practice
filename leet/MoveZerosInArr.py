class MoveZeros:
    @staticmethod
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroStart = 0
        runner = 0
        while runner < len(nums):
            if nums[runner] is not 0:
                if nums[zeroStart] is 0:
                    # swap
                    temp = nums[runner]
                    nums[runner] = nums[zeroStart]
                    nums[zeroStart] = temp
                if nums[zeroStart] is not 0:
                    zeroStart += 1
            runner += 1
        print(nums)
nums = [0, 1, 0, 3, 12]
print(nums)
MoveZeros.moveZeroes(nums)
print("\n")
nums = [1, 0, 1]
print(nums)
MoveZeros.moveZeroes(nums)
