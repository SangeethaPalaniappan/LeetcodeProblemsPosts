# 2914. Minimum Number of Changes to Make Binary String Beautiful

class Solution:
    def minChanges(self, s):
        sums = 0
        for i in range(0, len(s),2):
            if s[i + 1] != s[i]:
                sums += 1
        return sums        
