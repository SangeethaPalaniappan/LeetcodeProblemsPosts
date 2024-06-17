# 2264. Largest 3-Same-Digit Number in String

class Solution:
    def largestGoodInteger(self, num):
        start = 0
        maxi = 0
        change = 0 
        while start + 2 < len(num):
            if num[start] == num[start + 1] and num[start + 1] == num[start + 2] and num[start + 2] == num[start]:
                change = 1
                if maxi < int(num[start]):

                    maxi = int(num[start])
            start += 1  
        if change == 1: 
            number = str(maxi)    
            return number + number + number
        return ""        