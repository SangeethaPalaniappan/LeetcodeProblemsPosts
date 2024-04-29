# 2903. Find Indices With Index and Value Difference I

class Solution:
  def findIndices(self, nums, indexDifference, valueDifference):
    answer = [-1, -1]
    m = valueDifference
    n = indexDifference
    length = len(nums)
    for i in range(length - n):
        for j in range(i + n , length):
            if abs(i - j) >= n and abs(nums[i] - nums[j]) >= m:
                
                return [i , j]
    return answer    
