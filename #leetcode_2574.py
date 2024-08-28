# 2574. Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum  = [0] * len(nums)
        rightSum = [0] * len(nums)


        start = 0    
        sum_1 =
        for i in range(n):
            if i != 0:
                leftSum[i] = sum(nums[start : i])
            if i != n - 1:
                rightSum[i] = sum(nums[i + 1 : n])
   
        for j in range(n):
            nums[j] = abs(leftSum[j] - rightSum[j])

        return nums
