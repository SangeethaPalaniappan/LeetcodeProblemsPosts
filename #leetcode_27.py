# 27. Remove Element

class Solution:
    def removeElement(self, nums, val):

        c = len(nums)
        count = nums.count(val)
        for i in range(count):
            nums.remove(val)
        print(nums)        