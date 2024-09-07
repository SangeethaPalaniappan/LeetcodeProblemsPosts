# 3038. Maximum Number of Operations With the Same Score I

class Solution:
    def maxOperations(self, nums):
        tot = nums[0] + nums[1]
        count = 1
        for i in range(2, len(nums) - 1, 2):
            add = nums[i] + nums[i + 1]
            if tot == add:
                count += 1
            else:
                return count
        return count    
            
            
            
