# 8. String to Integer(atoi)

class Solution:
    def myAtoi(self, s):
        res = 0
        s = s.strip()
        change = 0
        iteration = 0
        for i in s:
            if iteration == 0 and ord(i) == 43:
                iteration = 1 
                continue
            if iteration == 0 and ord(i) == 45:
                iteration = 1 
                change = 1
                continue
            if ord(i) >= 48 and ord(i) <= 57:
                val = ord(i) - 48
                res = (res * 10) + val
            else:
                break   

            iteration = 1      
        if change == 1:
            res = -1 * res 
        if res > 2147483647:
            res = 2147483647
        if res < -2147483648:
            res = -2147483648             
        return res    
