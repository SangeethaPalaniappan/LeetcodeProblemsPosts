# 15. 3Sum

class Solution:
    def threeSum(self, nums):
        res_arr = []
        nums.sort()
        k = 0
        for i in range(len(nums)):
            if nums[k] > 0:
                break
            k = i    
            if i > 0 and nums[k] == nums[k - 1]:
                continue    
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tot = nums[i] + nums[left] + nums[right]
                if tot > 0:
                    right -= 1
                elif tot < 0:
                    left += 1
                else:
                    res_arr.append([nums[i], nums[left], nums[right]])     
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res_arr                 
