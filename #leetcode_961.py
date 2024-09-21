# 961. N-Repeated Element in Size 2N Array

class Solution:
    def repeatedNTimes(self, nums):
        hashset = set()
        for i in nums:
            if i not in hashset:
                hashset.add(i)
            else:
                return i
                
