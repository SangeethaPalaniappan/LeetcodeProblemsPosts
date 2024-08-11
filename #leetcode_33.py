# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid


            if nums[start] <= nums[mid]:

                if nums[mid] < nums[end]:
                    if nums[mid] < target:
                        start = mid + 1
                    else: # nums[mid] >= target:
                        end = mid - 1

                else: # nums[mid] >= nums[end]:
                    if target <= nums[mid]: 
                        if target >= nums[start]:
                            end = mid - 1

                        else: # target < nums[start]:             
                            start = mid + 1

                    else: # target > nums[mid]:
                        start = mid + 1            


            else: # nums[start] > nums[mid] and nums[mid] < nums[end]:            
                if target > nums[mid]:                
                    if target >= nums[start]:
                        end = mid - 1
                    else: # target < nums[start]:
                        start = mid + 1
                else: # target <= nums[mid]:
                    end = mid - 1
        return -1                        
