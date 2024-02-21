# 283. Move Zeros

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for num in range(n):
            if nums[num] != 0:
                nums[num], nums[i] = nums[i], nums[num]
                i += 1
                