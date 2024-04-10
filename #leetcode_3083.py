# 3083. Existenxe of a Substring and its Reverse

class Solution:
    def isSubstringPresent(self, s):
        dic = {}
        for i in range(len(s) - 1):
            m = s[i] + s[i + 1]
            dic[m] = 1
   
        s = s[:: -1]
        for j in range(len(s) - 1): 
            m = s[j] + s[j + 1]
            
            if m in dic:
                return 1
        return 0    