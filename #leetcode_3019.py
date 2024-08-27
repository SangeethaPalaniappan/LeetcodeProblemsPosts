# 3019. Number of Changing Keys

class Solution:
    def countKeyChanges(self, s):
        count = 0
        for key in range(len(s) - 1):
            if s[key].lower() != s[key + 1].lower():
                count += 1
        return count        
