# 2864. Maximum Odd Binary Number

class Solution:
    def maximumOddBinaryNumber(self, s):
        one  = s.count("1")
        zero = s.count("0")
        arr = ["0"] * len(s)
        arr[len(s) - 1] = "1"
        one -= 1
        n = len(s) - zero
        x = 0
        y = 0
        while x < n and y < one :
            arr[x] = "1"
            x += 1
            y += 1
            
        string = ""        
        for i in arr:
            string += i
        return string    
