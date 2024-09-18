# 3099. Harshad Number

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        tot = 0
        n = x
        while x > 0:
            rem = x % 10
            x //= 10
            tot += rem
        if n % tot == 0:
            return tot
        return -1            
