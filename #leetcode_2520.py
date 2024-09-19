# 2520. Count the Digits That Divide a Number

class Solution:
    def countDigits(self, num):
        n = num
        count = 0
        while num > 0:
            rem = num % 10
            if rem != 0 and n % rem == 0:
                count += 1
            num //= 10
        return count        
