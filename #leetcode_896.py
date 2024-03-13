# 896. Monotonic Array

class Solution:
    def isMonotonic(self, nums):
        init = 0 
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if init == -1:
                    return 0
                else:
                    init = 1
            elif nums[i] < nums[i + 1]:
                if init == 1:
                    return 0
                else:
                    init = -1
        return 1                            

