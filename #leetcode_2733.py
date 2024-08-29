# 2733. Neither Minimum nor Maximum

class Solution:
    def findNonMinOrMax(self, nums):
        if len(nums) == 2:
            return -1
        maxi = max(nums)
        mini = min(nums)
        for i in nums:
            if i != mini and i != maxi:
                return i
        return -1            
