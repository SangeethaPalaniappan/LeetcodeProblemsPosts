# 3131. Find the Integer Added to Array I

class Solution:
    def addedInteger(self, nums1, nums2):
        max_1 = max(nums1)
        max_2 = max(nums2)
        return max_2 - max_1
