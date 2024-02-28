# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums):
        start = 0
        end = len(nums) - 1
        ans = [0] * (end + 1)
        i = len(nums) - 1
        for s in range(len(nums)):
            if abs(nums[start]) > nums[end]:
                ans[i] = nums[start] ** 2
                start += 1
            else:
                ans[i] = nums[end] ** 2
                end -= 1
            i -= 1
        return ans        