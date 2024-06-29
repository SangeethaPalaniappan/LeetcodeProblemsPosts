# 41. First Missing Positive

class Solution:
    def firstMissingPositive(self, nums):
        mini = 1
        hashset = set()
        for i in nums:
            hashset.add(i)
        for j in range(len(nums)):
            if mini in hashset:
                mini += 1
            else:
                return mini    
        return mini
