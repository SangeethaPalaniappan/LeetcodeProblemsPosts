# 3210. Find the Encrypted String

class Solution:
    def getEncryptedString(self, s, k):
        if k > len(s):
            k = k % len(s)
        res = s[k : len(s)] + s[0 : k]
        return res
