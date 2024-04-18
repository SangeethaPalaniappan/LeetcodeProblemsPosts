# 713. Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        product = 1
        count = 0
        left, right = 0, 0
        n = len(nums)
        while right < n:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1    
        return count                