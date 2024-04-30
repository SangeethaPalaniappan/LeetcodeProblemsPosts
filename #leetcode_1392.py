# 1392. Longest Happy Prefix

class Solution:
    def longestPrefix(self, s):
        lhp = [0] * len(s)
        ans = ""    
        maxi = 0
        for i in range(1, len(s)):
            x = lhp[i - 1]
            while s[x] != s[i]:
                if x == 0:
                    x = -1
                    break
                else:
                    x = lhp[x - 1]    
            lhp[i] = x + 1 
            
        return s[len(s)-lhp[-1]:]