# 713. Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        product = 1
        count = 0
        left = 0
        n = len(nums)
        for right in range(n):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += 1 + (right - left)
   
        return count                