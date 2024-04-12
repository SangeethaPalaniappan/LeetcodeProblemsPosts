# 2185. Counting Words With a Given Prefix

class Solution:
    def prefixCount(self, words, pref):
        n = len(pref)
        count = 0
        for string in words:
            if string[0 : n] == pref:
                count += 1
        return count        