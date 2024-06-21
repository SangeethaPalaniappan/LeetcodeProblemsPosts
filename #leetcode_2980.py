# 2980. Check if Bitwise OR Has Trailing Zeros
class Solution:
    def hasTrailingZeros(self, nums):
        count = 0
        for num in nums:
            if num % 2 == 0:
                count += 1
            if count == 2:
                return 1         
        else:
            return 0
                