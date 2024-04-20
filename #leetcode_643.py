# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums, k):
        n = k
        if k == len(nums):
            return (sum(nums) / k)
        start = 0
        maxi = float('-inf')
        first_index = 0
        last_index = k

        tot = sum(nums[0 : k]) 
        avg = tot / n

        if maxi < avg:
            maxi = avg

        while last_index < len(nums):
            tot =  (tot - nums[first_index]) + nums[last_index]
            avg = tot / n
            if avg > maxi:
                maxi = avg
            k += 1
            first_index += 1
            last_index = k
        return maxi   