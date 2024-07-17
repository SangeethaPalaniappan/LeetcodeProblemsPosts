# 43. Multiply Strings

class Solution:
    def multiply(self, num1, num2):
        n1 = 0
        n2 = 0
        mul = 1
        for i in num1:
            n1 = (n1 * 10) + (ord(i) - 48)
        for j in num2:
            n2 = (n2 * 10) + (ord(j) - 48)
        mul = n1 * n2    
        return str(mul)    
