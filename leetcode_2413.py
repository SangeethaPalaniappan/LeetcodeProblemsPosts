# 2413. Smallest Even Multiple

class Solution:
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return n
        return n * 2    
