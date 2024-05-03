# 704. Binary Search

class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        return self.recursion(nums, low, high, target)

    def recursion(self, nums, low, high, target):

        if low <= high:   
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
                if high == len(nums):
                    return -1
                return self.recursion(nums, low, high, target)
            elif nums[mid] < target:
                low = mid + 1
                if low < 0:
                    return -1
                return self.recursion(nums, low, high, target)
        else:
            return -1        

