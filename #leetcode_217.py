# 217. Contains Duplicates

# Using Sorting

class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        for num in range(len(nums) - 1):
            if nums[num] == nums[num + 1]:
                return 1
        return 0    
      

# Using HashMap

class Solution:
    def containsDuplicate(self, nums):
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]] = 1
            else:
                return 1
        return 0          
    
# Using set() method
class Solution:
    def containsDuplicate(self, nums):
        if len(nums) != len(set(nums)):
            return 1
        return 0        