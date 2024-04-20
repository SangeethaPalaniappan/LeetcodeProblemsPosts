# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = k
        if k == len(nums):
            return (sum(nums) / k)
        start = 0
        maxi = float('-inf')
        tot = sum(nums[0 : k]) 
        avg = tot / n

        if maxi < avg:
            maxi = avg

        first_index = 0
        last_index = k
        while last_index < len(nums):
            tot =  (tot - nums[first_index]) + nums[last_index]
            avg = tot / n
            if avg > maxi:
                maxi = avg
            first_index += 1
            last_index += 1
        return maxi   