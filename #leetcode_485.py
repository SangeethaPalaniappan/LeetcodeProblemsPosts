# 485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left = 0
        right = 0
        count = 0
        maxi = 0
        while right < len(nums):
            if nums[right] == 1:
                count += 1
            else:
                left = right + 1 
                count = 0
            right += 1     
            maxi = max(count, maxi)
        return maxi        
