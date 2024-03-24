# 287. Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums):
        a = [0] * len(nums)

        for i in range(len(nums)):
            a[nums[i]] += 1

            if a[nums[i]] == 2:
                return nums[i] 