# 172. Factorial Trailing Zeroes

class Solution:
    def trailingZeroes(self, n):
        ans = 0
        x = 5
        while x <= n:
            div = n // x
            ans += div 
            x *= 5
        return ans    