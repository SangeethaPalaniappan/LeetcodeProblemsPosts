# 1528. Shuffle String
class Solution:
    def restoreString(self, s, indices):
        if len(s) == 1:
            return s
        arr = [-1] * len(s)
        for i in range(len(s)):
            arr[indices[i]] = s[i]
        string = ""
        for i in arr:
            string += i
        return string    
