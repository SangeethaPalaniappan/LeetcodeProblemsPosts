# 13. Roman to Integer

class Solution:
    def romanToInt(self, s):
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}    
        init = 0
        for c in range(len(s)):
            if c < len(s) - 1 and d[s[c]] < d[s[c + 1]]:
                init -= d[s[c]]
            else:
                init += d[s[c]]    
            
        return init

           
        