# 2903. Find Indices With Index and Value Difference I

class Solution:
  def findIndices(self, nums, indexDifference, valueDifference):
    min_ = 0
    max_ = 0
    min_max = []
    
    for i in range(len(nums)):
      if nums[i] < nums[min_]:
        min_ = i
      if nums[i] > nums[max_]:
        max_ = i
      min_max.append([min_, max_])

    for i in range(len(nums)):
      j = i - indexDifference
      if j >= 0:
        if abs(nums[i] - nums[min_max[j][0]]) >= valueDifference:
          return [min_max[j][0], i]
        if abs(nums[i] - nums[min_max[j][1]]) >= valueDifference:
          return [min_max[j][1], i]

    return [-1, -1]