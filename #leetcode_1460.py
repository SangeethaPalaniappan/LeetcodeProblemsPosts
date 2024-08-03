# 1460. Make Two Arrays Equal by Reversing Subarrays

class Solution:
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        if target == arr:
            return 1
        return 0    
