# 1460. Make Two Arrays Equal by Reversing Subarrays

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        if target == arr:
            return 1
        return 0    
