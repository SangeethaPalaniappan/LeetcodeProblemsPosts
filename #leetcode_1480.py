# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums):
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            nums[i] = tot
        return nums    
