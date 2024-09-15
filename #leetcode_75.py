# 75. Sort Colors

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            k = i
            j = k + 1
            while k >= 0 and j < len(nums):
                if nums[k] > nums[j]:
                    nums[k], nums[j] = nums[j], nums[k]
                    j -= 1
                k -= 1
            
