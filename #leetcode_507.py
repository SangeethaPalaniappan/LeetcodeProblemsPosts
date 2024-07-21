# 507. Perfect Number

class Solution:
    def checkPerfectNumber(self, num):
        if num % 2 == 1:
            return 0
        add = 1
        half = int((num ** 0.5)) + 1
        for i in range(2, half):
            if num % i == 0:
                add += i 
                div = num // i  
                if i != div:
                    add += div
                
        if add == num:      
            return 1
        return 0      
