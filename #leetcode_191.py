# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            m = n % 2
            n >>= 1
            if m == 1:
                count += 1
        return count        
        