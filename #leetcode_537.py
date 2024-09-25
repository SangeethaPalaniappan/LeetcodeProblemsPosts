# 537. Complex Number Multiplication

class Solution:
    def complexNumberMultiply(self, num1, num2):
        lis_1 = list(num1.split("+"))
        lis_2 = list(num2.split("+"))
        
        a = int(lis_1[0])
        b = int(lis_2[0])
        c = int(lis_2[1][0: len(lis_2[1]) - 1])
        d = int(lis_1[1][0: len(lis_1[1]) - 1])
        
        val_1 = a * b
        val_2 = a * c
        val_3 = c * d
        val_4 = b * d
        
        res = str(val_1 - val_3) +"+"+ str(val_2 + val_4) + "i"
        
        return res
        
