# 3151. Special Array I

class Solution:
    def isArraySpecial(self, nums):
        for i in range(len(nums) - 1):
            if (nums[i] % 2 == 0 and nums[i + 1] % 2 == 1) or (nums[i + 1] % 2 == 0 and nums[i] % 2 == 1):
                continue
            else:
                return 0
        return 1    