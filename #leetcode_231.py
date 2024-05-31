# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n):
        if n == 0:
            return 0
        if n & (n - 1) == 0:
            return 1    
        return 0

