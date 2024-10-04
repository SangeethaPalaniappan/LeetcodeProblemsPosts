# 3159. Find Occurrences of an Element in an Array

class Solution:
    def occurrencesOfElement(self, nums, queries, x):
        dic = {}
        arr = [-1] * len(queries)
        k = 1
        for i in range(len(nums)):
            if nums[i] == x:
                if nums[i] not in dic:
                    dic[k] = i
                    k += 1
                else:
                    dic[k] = i
                    k += 1
     
        if len(dic) == 0:
            return arr
        n = 0
        for l in queries:
            if l in dic:
                arr[n] = dic[l]
            else:
                arr[n] = -1
            n += 1
        return arr    
                    
