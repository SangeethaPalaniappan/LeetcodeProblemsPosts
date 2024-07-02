# 561. Array Partition

class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        tot = 0
        for i in range(0, len(nums), 2):
            mini = min(nums[i], nums[i + 1])
            tot += mini
        return tot    
