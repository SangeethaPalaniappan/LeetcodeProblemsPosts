# 229. Majority Element II

class Solution:
    def majorityElement(self, nums):
        arrs = []
        arr = {}
        n = len(nums) // 3
        for k in nums:
            if k not in arr:
                arr[k] = 1
            else:
                arr[k] += 1
        for j in arr.keys():
            get = arr.get(j)
            if n < get :
                arrs.append(j)    
        return arrs        

