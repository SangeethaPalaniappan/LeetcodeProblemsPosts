# 1876. Substrings of Size Three with Distinct Characters

class Solution:
    def countGoodSubstrings(self, s):
        i = 0
        count = 0
        while i + 2 < len(s):
            if s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i + 2] != s[i]:
                count += 1
            i += 1

        return count        
                