# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n):
        init = 0
        num = 1
        for iteration in range(n):            
            sum = init + num
            init = num
            num = sum
        return sum    
