# 3065.  Minimum Operations to Exceed Threshold Value I

class Solution:
    def minOperations(self, nums, k):
        count = 0
        for i in range(len(nums)):
            if nums[i] < k:
                count += 1
        return count        
