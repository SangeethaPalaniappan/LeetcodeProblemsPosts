# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                return mid
        if target < nums[0]:
            return 0
        return mid + 1         
