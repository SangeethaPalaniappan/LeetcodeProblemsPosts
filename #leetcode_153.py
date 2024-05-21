# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[start] <= nums[mid] and nums[start] < nums[end]:
                return nums[start]
            elif nums[start] > nums[end]:
                if nums[start] > nums[mid]:
                    if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                        return nums[mid + 1]
                    elif nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                        return nums[mid]
                    else:
                        end = mid - 1
                else:
                    start = mid + 1      
        return nums[start]                          