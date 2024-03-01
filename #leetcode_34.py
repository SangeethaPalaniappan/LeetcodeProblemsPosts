# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums, target):
        result = [-1, -1] 
        if len(nums) == 0:
            return result
        result[0] = self.search1(nums, target, 1)
        result[1] = self.search1(nums, target, 2)
        return result
        
    def search1(self, nums, target, k):
        index = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                if k == 1:
                    high = mid - 1
                elif k ==2:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index    

    



