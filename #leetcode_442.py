# 442. Find All Duplicats in an  Array

class Solution:
    def findDuplicates(self, nums):
        arr = []
        num_ind = [0] * (len(nums) + 1)
        for i in nums:
            num_ind[i] += 1
            if num_ind[i] == 2:
                arr.append(i)
        return arr        