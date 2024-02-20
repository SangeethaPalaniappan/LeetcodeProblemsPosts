# 268. Missing Number

class Solution:
    def missingNumber(self, nums):
        tot = 0
        for num in range(len(nums) + 1):
            tot += num
        sum = 0
        for num_in_arr in nums:
            sum += num_in_arr
        diff = tot - sum        
        return diff     