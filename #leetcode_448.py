# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums):
        arr = []
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1
            if nums[ind] > 0:    
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
                
    
        for k in range(len(nums)):
            if nums[k] > 0:
                arr.append(k + 1)
        return arr            
