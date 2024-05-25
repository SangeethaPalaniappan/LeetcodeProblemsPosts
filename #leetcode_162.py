# 162. Find Peak Element

class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
            