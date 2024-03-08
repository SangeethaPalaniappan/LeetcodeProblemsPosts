# 905. Sort Array By Parity

class Solution:
    def sortArrayByParity(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            while start < end and nums[start] % 2 == 0:
                start += 1
            while start < end and nums[end] % 2 == 1:
                end -= 1
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums        
            