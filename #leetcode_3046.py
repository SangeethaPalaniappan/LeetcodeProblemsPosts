# 3046. Split the Array

class Solution:
    def isPossibleToSplit(self, nums):
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                if dic[i] > 2:
                    return 0
        return 1
            
            
            
            