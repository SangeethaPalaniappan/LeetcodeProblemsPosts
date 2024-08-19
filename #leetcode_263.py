# 263. Ugly Number

class Solution:
    def isUgly(self, n):
        if n <= 0:
            return 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return 0
        return 1                    
