# 217. Contains Duplicates

class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        for num in range(len(nums) - 1):
            if nums[num] == nums[num + 1]:
                return 1
        return 0    
      