# 242. Valid Anagram

class Solution:
    def isAnagram(self, s, t):
        if len(s) > len(t) or len(t) > len(s):
            return 0
        has = {}
        for i in s:
            if i not in has:
                has[i] = 1
            else:
                has[i] += 1     
        for j in t:
            if j in has:
                has[j] -= 1
            else:
                return 0
        for k in has.values():
            if k != 0:
                return 0
        return 1