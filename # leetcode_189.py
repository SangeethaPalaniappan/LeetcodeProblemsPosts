# 189. Rotate Array

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)    
        ind = len(nums) - k
        ele = nums[ind : len(nums)]
        prev = nums[0 : ind]
        nums[0 : k] = ele
        nums[k : len(nums)] = prev

        