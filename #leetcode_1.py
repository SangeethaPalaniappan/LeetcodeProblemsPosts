class Solution:
    def twoSum(self, nums, target):
        d = {} # empty_hashmap 
        for i in range(len(nums)):
            m = target - nums[i]
            if m in d.keys():
                return [d.get(m), i]
            else:
                d[nums[i]] = i
            
        return []
