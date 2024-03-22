# 1464. Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums):
        maxi = 0
        for max_num in range(len(nums)):
            if nums[max_num] > maxi:
                maxi = nums[max_num]
                ind = max_num
        nums[ind] = 0       
        maxi_1 = 0        
        for max_num in nums:
            if max_num > maxi_1:
                maxi_1 = max_num        
        return (maxi - 1) * (maxi_1 - 1)        