# 3146. Permutation Difference between Two Strings

class Solution:
    def findPermutationDifference(self, s, t):
        tot = 0
        dic_1 = {}
        for i in range(len(s)):
            dic_1[s[i]] = i
        for j in range(len(t)):
            if t[j] in dic_1:
                tot += abs(dic_1[t[j]] - j)

        return tot    
            
