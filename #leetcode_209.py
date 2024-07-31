# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target, nums):
        l = 0
        r = 0
        tot = 0
        mini = float('inf')
        
        while r < len(nums):
            if r < len(nums) and tot < target:
                tot += nums[r]
                r += 1

            if l < r and tot >= target:
                index = r-l
                mini = min(index, mini)
                tot -= nums[l]
                l += 1
                
            
        if mini == float('inf'):
            return 0
        return mini      
