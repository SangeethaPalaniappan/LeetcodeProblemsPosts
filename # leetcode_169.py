# 169. Majority Element

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums) // 2
        return nums[n]