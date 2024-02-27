# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s, t):
        length = len(t)
        init = 0
        count = 0
        while init < length and count < len(s):
            if s[count] == t[init]:
                count += 1

            init += 1    
        if len(s) == count:
            return 1
        return 0        
